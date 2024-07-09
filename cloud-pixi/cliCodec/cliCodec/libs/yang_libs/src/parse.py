import os
import json
import copy
import yaml

from libs.yang_libs.src.model import Module, Grouping, Container, List, Leaf, Augment
from libs.yang_libs.src.util import listify


class GXParser(object):

    module_data = dict()
    sub_module_data = dict()
    current_module = ''

    def __init__(self, base_dir, recipe, filter=None):
        self.module_data, self.sub_module_data = self._build_module_data(base_dir)
        self.recipe = recipe
        self.pixi_module_list = list()
        if 'map' not in os.listdir(base_dir):
            os.mkdir(os.path.join(base_dir, 'map'))
        if 'rpc' not in os.listdir(base_dir):
            os.mkdir(os.path.join(base_dir, 'rpc'))
        for k, v in self.module_data.items():
            if filter is None or filter == k:
                self.current_module = k
                pixi_module = Module(k, v['@name'], base_dir)
                self.pixi_module_list.append(pixi_module)
                if 'namespace' in v:
                    pixi_module.namespace = v['namespace']['@uri']
                if 'grouping' in v:
                    for grouping in listify(v['grouping']):
                        self.process_grouping(grouping, pixi_module)
                if 'container' in v:
                    for container in listify(v['container']):
                        self.process_container(container, pixi_module)
                if 'list' in v:
                    for list_item in listify(v['list']):
                        self.process_list(list_item, pixi_module)
                if 'augment' in v:
                    for augment in listify(v['augment']):
                        self.process_augment(augment, pixi_module)
                if 'identity' in v:
                    for i in listify(v['identity']):
                        id_item = {
                            'name': i['@name'],
                            'base': i['base']['@name'] if 'base' in i else None
                        }
                        pixi_module.identities.append(id_item)
                if 'rpc' in v:
                    for rpc in listify(v['rpc']):
                        self.process_rpc(rpc, pixi_module)

    def _build_module_data(self, base_dir):
        module_data = dict()
        sub_module_data = dict()
        source_path = os.path.join(base_dir, 'json')
        for source in os.listdir(source_path):
            with open(os.path.join(source_path, source)) as fh:
                read_data = json.load(fh)
                if 'module' in read_data:
                    module_data[read_data['module']['prefix']['@value']] = read_data['module']
                elif 'submodule' in read_data:
                    sub_module_data[read_data['submodule']['@name']] = read_data['submodule']
        return module_data, sub_module_data

    def process_grouping(self, grouping, pixi_object, merge=False):
        if merge:
            pixi_grouping = pixi_object
        else:
            pixi_grouping = pixi_object.add_grouping(grouping)
        if 'leaf' in grouping:
            for leaf in listify(grouping['leaf']):
                self.process_leaf(leaf, pixi_grouping)
        if 'leaf-list' in grouping:
            for leaf in listify(grouping['leaf-list']):
                self.process_leaf(leaf, pixi_grouping, isList=True)
        if 'container' in grouping:
            for container in listify(grouping['container']):
                self.process_container(container, pixi_grouping)
        if 'list' in grouping:
            for list_item in listify(grouping['list']):
                self.process_list(list_item, pixi_grouping)
        if 'uses' in grouping:
            for use in listify(grouping['uses']):
                self.process_use(use, pixi_grouping)

    def process_container(self, container, pixi_object):
        pixi_container = pixi_object.add_container(container)
        if 'leaf' in container:
            for leaf in listify(container['leaf']):
                self.process_leaf(leaf, pixi_container)
        if 'leaf-list' in container:
            for leaf in listify(container['leaf-list']):
                self.process_leaf(leaf, pixi_container, isList=True)
        if 'container' in container:
            for sub_container in listify(container['container']):
                self.process_container(sub_container, pixi_container)
        if 'list' in container:
            for list_item in listify(container['list']):
                self.process_list(list_item, pixi_container)
        if 'uses' in container:
            for use in listify(container['uses']):
                self.process_use(use, pixi_container)

    def process_list(self, list_item, pixi_object):
        pixi_list = pixi_object.add_list(list_item)
        if 'leaf' in list_item:
            for leaf in listify(list_item['leaf']):
                self.process_leaf(leaf, pixi_list)
        if 'leaf-list' in list_item:
            for leaf in listify(list_item['leaf-list']):
                self.process_leaf(leaf, pixi_list, isList=True)
        if 'container' in list_item:
            for container in listify(list_item['container']):
                self.process_container(container, pixi_list)
        if 'list' in list_item:
            for list_sub_item in listify(list_item['list']):
                self.process_list(list_sub_item, pixi_list)
        if 'uses' in list_item:
            for use in listify(list_item['uses']):
                self.process_use(use, pixi_list)

    def process_leaf(self, leaf, pixi_object, isList=False):
        type_data = self.process_type(leaf['type'])
        pixi_object.add_leaf(leaf, type_data, isList)

    def process_type(self, type):
        def _map_type(type):
            result = dict()
            if type['@name'] in ['string', 'decimal64', 'instance-identifier']:
                result['ptype'] = 'str'
            elif type['@name'] in ['yang:date-and-time', 'yang:dotted-quad', 'yang:hex-string']:
                result['ptype'] = 'str'
            elif type['@name'] in ['yang:counter64', 'yang:zero-based-counter64']:
                result['ptype'] = 'int'
            elif type['@name'] == 'enumeration':
                result['ptype'] = 'str'
                vals = [e['@name'] for e in listify(type['enum'])]
                result['values'] = vals
            elif type['@name'] == 'boolean':
                result['ptype'] = 'bool'
            elif type['@name'] == 'union':
                # Assume str for now
                result['ptype'] = 'str'
            elif type['@name'] in ['uint8', 'uint16', 'uint32', 'uint64', 'int8', 'int16', 'int32', 'int64']:
                result['ptype'] = 'int'
            elif type['@name'].startswith('inet:'):
                result['ptype'] = 'str'
            elif type['@name'] == 'leafref':
                result['ptype'] = 'unknown'
                result['leafref'] = type['path']['@value']
            elif type['@name'] == 'identityref':
                result['ptype'] = 'str'
                result['identityref'] = type['base']['@name']
            return result

        type_result = _map_type(type)
        if 'ptype' not in type_result:
            if ':' in type['@name']:
                # External type
                module_name, type_name = type['@name'].split(':')
                if module_name in self.module_data:
                    module = self.module_data[module_name]
                    if 'typedef' in module:
                        found_type = [t for t in listify(module['typedef']) if t['@name'] == type_name]
                        if found_type:
                            type_result = _map_type(found_type[0]['type'])
                if 'ptype' not in type_result:
                    type_result['ptype'] = 'str'
            else:
                module = self.module_data[self.current_module]
                if 'typedef' in module:
                    found_type = [t for t in listify(module['typedef']) if t['@name'] == type['@name']]
                    if found_type:
                        type_result = _map_type(found_type[0]['type'])
                if 'ptype' not in type_result:
                    type_result['ptype'] = 'str'
        return type_result

    def process_use(self, use, pixi_object):
        use = use['@name']
        if ':' in use:
            # External use
            module_name, group_name = use.split(':')
            if module_name in self.module_data:
                module = self.module_data[module_name]
                found_grouping = [g for g in listify(module['grouping']) if g['@name'] == group_name]
                if found_grouping:
                    old_module = self.current_module
                    self.current_module = module_name
                    self.process_grouping(found_grouping[0], pixi_object, merge=True)
                    self.current_module = old_module
            else:
                #print(f"Warning: Cannot find module {module_name}")
                pass
        else:
            # Internal use
            module = self.module_data[self.current_module]
            found_grouping = [g for g in listify(module['grouping']) if g['@name'] == use]
            if found_grouping:
                self.process_grouping(found_grouping[0], pixi_object, merge=True)
            else:
                if 'include' in module:
                    for include in listify(module['include']):
                        submodule = self.sub_module_data[include['@module']]
                        found_grouping = [g for g in listify(submodule['grouping']) if g['@name'] == use]
                        if found_grouping:
                            self.process_grouping(found_grouping[0], pixi_object, merge=True)

    def process_augment(self, augment, pixi_object):
        pixi_object.add_augment(augment)

    def process_rpc(self, rpc, pixi_object):
        pixi_rpc = pixi_object.add_rpc(rpc)
        if 'input' in rpc:
            if 'leaf' in rpc['input']:
                for leaf in listify(rpc['input']['leaf']):
                    self.process_leaf(leaf, pixi_rpc)
            if 'leaf-list' in rpc['input']:
                for leaf in listify(rpc['input']['leaf-list']):
                    self.process_leaf(leaf, pixi_rpc, isList=True)
            if 'list' in rpc['input']:
                for list_item in listify(rpc['input']['list']):
                    self.process_list(list_item, pixi_rpc)
            if 'uses' in rpc['input']:
                for use in listify(rpc['input']['uses']):
                    self.process_use(use, pixi_rpc)
            if 'choice' in rpc['input']:
                for choice in listify(rpc['input']['choice']):
                    self.process_choice(choice, pixi_rpc)

    def process_choice(self, choice, pixi_object):
        if 'leaf' in choice:
            for leaf in listify(choice['leaf']):
                self.process_leaf(leaf, pixi_object)
        if 'leaf-list' in choice:
            for leaf in listify(choice['leaf']):
                self.process_leaf(leaf, pixi_object, isList=True)
        if 'case' in choice:
            for case in listify(choice['case']):
                self.process_case(case, pixi_object)

    def process_case(self, case, pixi_object):
        pixi_case = pixi_object.add_case(case)
        if 'leaf' in case:
            for leaf in listify(case['leaf']):
                self.process_leaf(leaf, pixi_case)
        if 'leaf-list' in case:
            for leaf in listify(case['leaf-list']):
                self.process_leaf(leaf, pixi_case, isList=True)

    def print_map(self):
        for module in self.pixi_module_list:
            module.print_map()

    def process_leafrefs(self):
        for module in self.pixi_module_list:
            module.process_leafrefs()

    def process_identityrefs(self):
        def _process_block(block, module):
            if isinstance(block, Module):
                for k, v in block.groupings.items():
                    _process_block(v, module)
                for k, v in block.containers.items():
                    _process_block(v, module)
                for k, v in block.lists.items():
                    _process_block(v, module)
            elif isinstance(block, Grouping) or isinstance(block, Container) or isinstance(block, List):
                for k, v in block.containers.items():
                    _process_block(v, module)
                for k, v in block.lists.items():
                    _process_block(v, module)
                for k, v in block.leafs.items():
                    _process_leaf(v, module)
        def _process_leaf(leaf, module):
            if 'identityref' in leaf.type:
                if ':' in leaf.type['identityref']:
                    # External
                    ext_name, ref_name = leaf.type['identityref'].split(':')
                    found_mod = [m for m in self.pixi_module_list if m.name == ext_name]
                    if found_mod:
                        ext_module = found_mod[0]
                        found_id = [i for i in ext_module.identities if i['name'] == ref_name]
                        if found_id:
                            ext_id = found_id[0]
                            found_default = [i for i in ext_module.identities if i['base'] == ext_id['name']]
                            if found_default:
                                leaf.default_value = found_default[0]['name']
                            if 'values' in ext_id:
                                leaf.type['values'] = ext_id['values']
                            leaf.namespace = {
                                'namespace': ext_module.namespace,
                                'prefix': ext_name
                            }
                else:
                    found_id = [i for i in module.identities if i['name'] == leaf.type['identityref']]
                    if found_id:
                        ext_id = found_id[0]
                        found_default = [i for i in module.identities if i['base'] == ext_id['name']]
                        if found_default:
                            leaf.default_value = found_default[0]['name']
                            leaf.type['values'] = [i['name'] for i in found_default]
                        leaf.namespace = {
                            'namespace': module.namespace,
                            'prefix': None
                        }
        # Connect identities to base
        for mod in self.pixi_module_list:
            for identity in mod.identities:
                # Find base identity
                if identity['base'] and ':' in identity['base']:
                    ext_name, id_name = identity['base'].split(':')
                    found_mod = [m for m in self.pixi_module_list if m.name == ext_name]
                    if found_mod:
                        ext_module = found_mod[0]
                        found_id = [i for i in ext_module.identities if i['name'] == id_name]
                        if found_id:
                            found_id = found_id[0]
                            if 'values' not in found_id:
                                found_id['values'] = []
                            found_id['values'].append(identity['name'])
        for mod in self.pixi_module_list:
            _process_block(mod, mod)
    
    def process_deviations(self, dev_mod_list):
        for mod in dev_mod_list:
            dev_module = self.module_data[mod]
            if 'deviation' in dev_module:
                for deviation in dev_module['deviation']:
                    split_path = deviation['@target-node'].split('/')
                    if split_path[0] == '':
                        split_path.remove('')
                    module_name = split_path[0].split(':')[0]
                    found_src = [m for m in self.pixi_module_list if m.name == module_name]
                    if found_src:
                        src_module = found_src[0]
                        obj = self.find_object_by_path(src_module, deviation['@target-node'])
                        if obj:
                            if deviation['deviate']['@value'] == 'not-supported':
                                obj.supported = False
                            elif deviation['deviate']['@value'] in ['add', 'replace']:
                                if 'config' in deviation['deviate']:
                                    obj.config = False if deviation['deviate']['config']['@value'] == "false" else True
                                if 'mandatory' in deviation['deviate']:
                                    obj.mandatory = True if deviation['deviate']['mandatory']['@value'] == "true" else False

    def merge_augments(self, src_module, augments, combo_name):
        new_modules = list()
        found_src = [m for m in self.pixi_module_list if m.name == src_module]
        if found_src:
            src = found_src[0]
            src_copy = copy.deepcopy(src)
            src_copy.name = src.name + '-' + combo_name
            src_copy.full_name = src.full_name + '-' + combo_name
            src_copy.set_filepath()

            for aug in augments:
                dest_module = aug['module']
                found_dest = [m for m in self.pixi_module_list if m.name == dest_module]
                if found_dest:
                    dest = found_dest[0]
                    augment = dest.augments[aug['targetNode']]
                    for use in aug['uses']:
                        if use not in augment.uses:
                            print("Error")
                            raise ValueError("Error")
                        if use in dest.groupings:
                            obj = self.find_object_by_path(src_copy, aug['targetNode'])
                            target = copy.deepcopy(dest.groupings[use])
                            target_namespace = {
                                'namespace': dest.namespace,
                                'prefix': None
                            }
                            target.set_namespace(target_namespace)
                            self.merge_target_to_host(obj, target)
            self.pixi_module_list.append(src_copy)

    def connect_augments(self):
        new_modules = list()
        for module in self.pixi_module_list:
            if module.name == 'infinera-oc-ext':
                k = '/oc-platform:components/oc-platform:component/oc-platform:config'
                v = module.augments[k]
                #for k, v in module.augments.items():
                split_path = k.split('/')
                if split_path[0] == '':
                    split_path.remove('')
                module_name = split_path[0].split(':')[0]
                found_module = [m for m in self.pixi_module_list if m.name == module_name]
                if found_module:
                    if v.uses:
                        for use in v.uses:
                            if use in module.groupings:
                                new_module = copy.deepcopy(found_module[0])
                                obj = self.find_object_by_path(new_module, k)
                                self.merge_target_to_host(obj, module.groupings[use])
                                new_module.name = module.name + '-' + use.split('-')[0]
                                new_module.full_name = module.full_name + '-' + use.split('-')[0]
                                new_module.set_filepath()
                                #module.name = 'remove_' + module.name
                                #module.full_name = 'remove_' + module.full_name
                                #print(module.full_name)
                                #module.set_filepath()
                                new_modules.append(new_module)
        self.pixi_module_list += new_modules                

    def merge_target_to_host(self, host, target):
        for k, v in target.containers.items():
            host.containers[k] = v
        for k, v in target.lists.items():
            host.lists[k] = v
        for k, v in target.leafs.items():
            host.leafs[k] = v

    def find_object_by_path(self, module, path):
        def find_child_of_object(obj, target):
            if isinstance(obj, Module):
                for k, v in obj.groupings.items():
                    result = find_child_of_object(v, target)
                    if result:
                        return result
            for k, v in obj.containers.items():
                if k == target:
                    return v
            for k, v in obj.lists.items():
                if k == target:
                    return v
            for k, v in obj.leafs.items():
                if k == target:
                    return v
            return False
        split_path = path.split('/')
        if split_path[0] == '':
            split_path.remove('')
        traverse_obj = module
        for path_bit in split_path:
            if ':' in path_bit:
                target_item = path_bit.split(':')[1]
            else:
                target_item = path_bit
            traverse_obj = find_child_of_object(traverse_obj, target_item)
            if traverse_obj is False:
                return traverse_obj
        return traverse_obj

    def build_object_by_path(self, module, path, out_dict):
        def find_child_of_object(obj, target):
            if isinstance(obj, Module):
                for k, v in obj.groupings.items():
                    result = find_child_of_object(v, target)
                    if result:
                        return result
            for k, v in obj.containers.items():
                if k == target:
                    return v
            for k, v in obj.lists.items():
                if k == target:
                    return v
            for k, v in obj.leafs.items():
                if k == target:
                    return v
            return False
        split_path = path.split('/')
        if split_path[0] == '':
            split_path.remove('')
        traverse_obj = module
        traverse_dict = out_dict
        for path_bit in split_path:
            if ':' in path_bit:
                target_item = path_bit.split(':')[1]
            else:
                target_item = path_bit
            traverse_obj = find_child_of_object(traverse_obj, target_item)
            if isinstance(traverse_obj, Container):
                traverse_dict[traverse_obj.name] = dict()
                traverse_dict = traverse_dict[traverse_obj.name]
            elif isinstance(traverse_obj, List):
                traverse_dict[traverse_obj.name] = list()
                if len(traverse_obj.key.split()) > 1:
                    leaf = traverse_obj.leafs[traverse_obj.key.split()[0]]
                else:
                    leaf = traverse_obj.leafs[traverse_obj.key]
                key_leaf = {
                    'type': leaf.type,
                    'isList': leaf.isList,
                    'description': leaf.description,
                    'key': True,
                    'mandatory': leaf.mandatory,
                    'config': leaf.config,
                    'default': leaf.default_value,
                    'hardcode': False
                }
                if leaf.namespace != '':
                    key_leaf['namespace'] = leaf.namespace
                traverse_dict[traverse_obj.name].append({traverse_obj.key: key_leaf})
                traverse_dict = traverse_dict[traverse_obj.name][0]

    def output_example(self, module, path):
        """
        output_example _summary_

        Generates example data for 

        :param module: _description_
        :type module: _type_
        :param path: _description_
        :type path: _type_
        :return: _description_
        :rtype: _type_
        """
        TOP_LEVEL = {
            "components": "http://openconfig.net/yang/platform",
            "terminal-device": "http://openconfig.net/yang/terminal-device",
            "system": "http://openconfig.net/yang/system",
        }
        def process_node(node, example, hierarchy):
            if node.namespace:
                namespace = node.namespace
            for k, v in node.containers.items():
                new_hierarchy = []
                new_hierarchy += hierarchy
                new_hierarchy.append(v)
                process_node(v, example, new_hierarchy)
            for k, v in node.lists.items():
                new_hierarchy = []
                new_hierarchy += hierarchy
                new_hierarchy.append(v)
                process_node(v, example, new_hierarchy)
            if len(node.leafs) > 0:
                # Wonky condition for openconfig
                h_list = [h.name for h in hierarchy]
                if 'config' in h_list and 'properties' not in h_list and 'subcomponents' not in h_list or 'infinera' in self.recipe:
                    traverse_ex = example
                    for h in hierarchy:
                        if (isinstance(h, Container) or isinstance(h, List)) and not h.config:
                            return
                        if h not in traverse_ex:
                            if isinstance(h, Container):
                                if h.namespace:
                                    traverse_ex[h.name] = {'namespace': h.namespace}
                                else:
                                    traverse_ex[h.name] = dict()
                                traverse_ex = traverse_ex[h.name]
                            elif isinstance(h, List):
                                traverse_ex[h.name] = list()
                                keys = h.key.split(' ')
                                elem = dict()
                                for key in keys:
                                    leaf = h.leafs[key]
                                    elem[key] = {
                                        'type': leaf.type,
                                        'isList': leaf.isList,
                                        'description': leaf.description,
                                        'key': True,
                                        'mandatory': leaf.mandatory,
                                        'config': leaf.config,
                                        'default': leaf.default_value,
                                        'hardcode': False
                                    }
                                    if leaf.namespace != '':
                                        elem['namespace'] = leaf.namespace
                                traverse_ex[h.name].append(elem)
                                traverse_ex = traverse_ex[h.name][0]
                        else:
                            if isinstance(h, Container):
                                traverse_ex = traverse_ex[h.name]
                            elif isinstance(h, List):
                                traverse_ex = traverse_ex[h.name][0]
                    for k, v in node.leafs.items():
                        if k not in traverse_ex:
                            traverse_ex[k] = {
                                'type': v.type,
                                'isList': v.isList,
                                'description': v.description,
                                'mandatory': v.mandatory,
                                'key': False,
                                'config': v.config,
                                'default': v.default_value,
                                'hardcode': False
                            }
                            if v.namespace != '':
                                traverse_ex[k]['namespace'] = v.namespace
                            #elif namespace != '':
                            #    traverse_ex[k]['namespace'] = namespace
        found_module = [m for m in self.pixi_module_list if m.name == module]
        base_example = {}
        self.build_object_by_path(found_module[0], path, base_example)
        base_obj = self.find_object_by_path(found_module[0], path)
        #print(json.dumps(base_obj, indent=4))
        traverse_ex = base_example
        for path_bit in path.split('/'):
            if path_bit in TOP_LEVEL:
                traverse_ex[path_bit]['namespace'] = {"prefix": None, "namespace": TOP_LEVEL[path_bit]}
            if isinstance(traverse_ex[path_bit], dict):
                traverse_ex = traverse_ex[path_bit]
            elif isinstance(traverse_ex[path_bit], list):
                traverse_ex = traverse_ex[path_bit][0]
        hierarchy = []
        process_node(base_obj, traverse_ex, hierarchy)
        return base_example

    def output_rpcs(self, base_path):
        for module in self.pixi_module_list:
            for rpc_name, rpc_data in module.rpcs.items():
                output = {
                    "namespace": module.namespace,
                    "inputs": {},
                    "cases": {}
                }
                for k, v in rpc_data.leafs.items():
                    output['inputs'][k] = {
                        'type': v.type,
                        'isList': v.isList,
                        'description': v.description,
                        'mandatory': v.mandatory
                    }
                for lk, lv in rpc_data.lists.items():
                    list_item = {}
                    for k, v in lv.leafs.items():
                        list_item[k] = {
                            'type': v.type,
                            'isList': v.isList,
                            'description': v.description,
                            'mandatory': v.mandatory
                        }
                    output['inputs'][lk] = [list_item]
                for ck, cv in rpc_data.cases.items():
                    case_item = {}
                    for k, v in cv.leafs.items():
                        case_item[k] = {
                            'type': v.type,
                            'isList': v.isList,
                            'description': v.description,
                            'mandatory': v.mandatory
                        }
                    output['cases'][ck] = case_item
                with open(os.path.join(base_path, 'rpc', f"{rpc_name}.json"), 'w') as fh:
                    json.dump(output, fh, indent=4)


class XRParser(object):

    yaml_master_data = {}

    def __init__(self, base_path):
        self.base_path = base_path
        in_dirs = os.listdir(os.path.join(self.base_path, 'yaml'))
        self._fill_master_data()

    def process_all_schemas(self):
        self.output_schemas = dict()
        for module_name, module_val in self.yaml_master_data.items():
            for schema_name, schema_val in module_val.get('components', {}).get('schemas', {}).items():
                self.output_schemas[schema_name] = dict()
                if 'properties' in schema_val:
                    self.output_schemas[schema_name] = self.expand_object(module_name, schema_val)
                elif 'items' in schema_val:
                    self.output_schemas[schema_name] = self.expand_array(module_name, schema_val)
        with open(os.path.join(self.base_path, 'schemas.json'), 'w') as fh:
            json.dump(self.output_schemas, fh, indent=4)

    def process_all_paths(self):
        self.output_paths = dict()
        for module_name, module_val in self.yaml_master_data.items():
            for path_name, path_val in module_val.get('paths', {}).items():
                self.output_paths[path_name] = dict()
                if 'parameters' in path_val:
                    self.output_paths[path_name]['parameters'] = self.expand_parameters(module_name, path_val['parameters'])
                if 'get' in path_val:
                    self.output_paths[path_name]['get'] = {
                        'summary': path_val['get'].get('summary', None),
                    }
                if 'post' in path_val:
                    self.output_paths[path_name]['post'] = {
                        'summary': path_val['post'].get('summary', None),
                        'requestBody': path_val['post']['requestBody']
                    }
                if 'put' in path_val:
                    self.output_paths[path_name]['put'] = {
                        'summary': path_val['put'].get('summary', None),
                        'requestBody': path_val['put']['requestBody']
                    }
                if 'delete' in path_val:
                    self.output_paths[path_name]['delete'] = {
                        'summary': path_val['delete'].get('summary', None)
                    }
        with open(os.path.join(self.base_path, 'paths.json'), 'w') as fh:
            json.dump(self.output_paths, fh, indent=4)

    def expand_object(self, current_module, object_in):
        object_out = {k: v for k, v in object_in.items() if k != 'properties'}
        object_out['properties'] = dict()
        for k, v in object_in.get('properties', {}).items():
            if '$ref' in v:
                ref_module, ref = self._get_ref(current_module, v['$ref'])
                if ref.get('type') == 'object':
                    object_out['properties'][k] = self.expand_object(ref_module, ref)
                elif ref.get('properties'):
                    object_out['properties'][k] = self.expand_object(ref_module, ref)
                elif ref.get('type') == 'array':
                    object_out['properties'][k] = self.expand_array(ref_module, ref)
                else:
                    object_out['properties'][k] = ref
            elif v.get('type') == 'object':
                object_out['properties'][k] = self.expand_object(current_module, v)
            elif v.get('type') == 'array':
                object_out['properties'][k] = self.expand_array(current_module, v)
            else:
                object_out['properties'][k] = v
        return object_out

    def expand_array(self, current_module, array_in):
        array_out = {k: v for k, v in array_in.items() if k != 'items'}
        array_out['items'] = dict()
        if '$ref' in array_in['items']:
            ref_module, ref = self._get_ref(current_module, array_in['items']['$ref'])
            if ref.get('type') == 'object':
                array_out['items'] = self.expand_object(ref_module, ref)
            elif ref.get('properties'):
                array_out['items'] = self.expand_object(ref_module, ref)
            elif ref.get('type') == 'array':
                array_out['items'] = self.expand_array(ref_module, ref)
            else:
                array_out['items'] = ref
        elif array_in['items'].get('type') == 'object':
            array_out['items'] = self.expand_object(current_module, array_in['items'])
        elif array_in['items'].get('type') == 'array':
            array_out['items'] = self.expand_array(current_module, array_in['items'])
        else:
            array_out['items'] = array_in['items']
        return array_out

    def expand_parameters(self, module_name, parameters):
        parsed_params = dict()
        for param in parameters:
            if '$ref' in param:
                param_name = param['$ref'].split('/')[-1]
                ref_module, ref = self._get_ref(module_name, param['$ref'])
                parsed_params[param_name] = ref
        return parsed_params

    def _get_ref(self, module_name, ref_name):
        if ref_name.startswith('#'):
            # Local
            data = self._get_xpath(self.yaml_master_data[module_name], ref_name[1:])
        else:
            # External
            filepath = ref_name.split('#')[0]
            module_name = filepath.split('/')[-1]
            file_data = self.yaml_master_data[module_name]
            data = self._get_xpath(file_data, ref_name.split('#')[1])
        return module_name, data

    def _get_xpath(self, data, xpath):
        traverse_dict = data
        for p in xpath.split('/')[1:]:
            if p in traverse_dict:
                traverse_dict = traverse_dict[p]
            else:
                print(f"Error: {p} not found in data")
                return None
        return traverse_dict

    def _fill_master_data_old(self):
        for d in os.listdir(os.path.join(self.base_path, 'yaml')):
            for y in os.listdir(os.path.join(self.base_path, 'yaml', d, 'v1')):
                with open(os.path.join(self.base_path, 'yaml', d, 'v1', y)) as fh:
                    self.yaml_master_data[y] = yaml.safe_load(fh)

    def _fill_master_data(self):
        for y in os.listdir(os.path.join(self.base_path, 'yaml')):
            with open(os.path.join(self.base_path, 'yaml', y)) as fh:
                self.yaml_master_data[y] = yaml.safe_load(fh)

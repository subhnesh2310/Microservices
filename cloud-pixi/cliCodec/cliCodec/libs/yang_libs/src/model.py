import os

from libs.yang_libs.src.util import listify


class PIXIBase(object):

    def print(self, string, filepath):
        with open(filepath, 'a') as fh:
            fh.write(string + '\n')
        #print(string)


class Module(PIXIBase):

    def __init__(self, name, full_name, base_dir):
        self.groupings = {}
        self.containers = {}
        self.lists = {}
        self.augments = {}
        self.rpcs = {}
        self.identities = []
        self.name = name
        self.full_name = full_name
        self.base_dir = base_dir
        self.namespace = None
        self.filepath = os.path.join(self.base_dir, 'map', f'{self.full_name}.txt')
    
    def set_filepath(self):
        self.filepath = os.path.join(self.base_dir, 'map', f'{self.full_name}.txt')
    
    def add_grouping(self, grouping_data):
        self.groupings[grouping_data['@name']] = Grouping(grouping_data)
        return self.groupings[grouping_data['@name']]

    def add_container(self, container_data):
        self.containers[container_data['@name']] = Container(container_data)
        return self.containers[container_data['@name']]

    def add_list(self, list_data):
        self.lists[list_data['@name']] = List(list_data)
        return self.lists[list_data['@name']]

    def add_augment(self, augment_data):
        self.augments[augment_data['@target-node']] = Augment(augment_data)
        return self.augments[augment_data['@target-node']]

    def add_rpc(self, rpc_data):
        self.rpcs[rpc_data['@name']] = RPC(rpc_data)
        return self.rpcs[rpc_data['@name']]

    def print_map(self):
        with open(self.filepath, 'w') as fh:
            pass
        self.print(self.name, self.filepath)
        for k, v in self.groupings.items():
            v.print_map(1, self)
        for k, v in self.containers.items():
            v.print_map(1, self)

    def process_leafrefs(self):
        hierarchy = []
        for k, v in self.groupings.items():
            v.process_leafrefs(hierarchy)


class Grouping(PIXIBase):

    def __init__(self, grouping_data):
        self.name = grouping_data['@name']
        self.containers = {}
        self.lists = {}
        self.leafs = {}
        self.namespace = None

    def add_container(self, container_data):
        self.containers[container_data['@name']] = Container(container_data)
        return self.containers[container_data['@name']]

    def add_list(self, list_data):
        self.lists[list_data['@name']] = List(list_data)
        return self.lists[list_data['@name']]

    def add_leaf(self, leaf_data, type, isList):
        self.leafs[leaf_data['@name']] = Leaf(leaf_data, type, isList)

    def print_map(self, spacing, module):
        for k, leaf in self.leafs.items():
            leaf.print_map(spacing, module)
        for k, container in self.containers.items():
            container.print_map(spacing, module)
        for k, list_item in self.lists.items():
            list_item.print_map(spacing, module)

    def process_leafrefs(self, hierarchy):
        new_hierarchy = []
        new_hierarchy += hierarchy
        new_hierarchy.append(self)
        for k, v in self.containers.items():
            v.process_leafrefs(new_hierarchy)
        for k, v in self.lists.items():
            v.process_leafrefs(new_hierarchy)
        for k, v in self.leafs.items():
            v.process_leafrefs(new_hierarchy)

    def set_namespace(self, namespace):
        for k, v in self.containers.items():
            v.namespace = namespace
        for k, v in self.lists.items():
            v.namespace = namespace
        for k, v in self.leafs.items():
            v.namespace = namespace


class Container(PIXIBase):

    def __init__(self, container_data):
        self.name = container_data['@name']
        self.description = container_data['description']['text'] if 'description' in container_data else None
        self.config = False if 'config' in container_data and container_data['config']['@value'] == "false" else True
        self.containers = {}
        self.lists = {}
        self.leafs = {}
        self.supported = True
        self.namespace = None
    
    def add_container(self, container_data):
        self.containers[container_data['@name']] = Container(container_data)
        return self.containers[container_data['@name']]

    def add_list(self, list_data):
        self.lists[list_data['@name']] = List(list_data)
        return self.lists[list_data['@name']]

    def add_leaf(self, leaf_data, type, isList):
        self.leafs[leaf_data['@name']] = Leaf(leaf_data, type, isList)

    def print_map(self, spacing, module):
        tabStr = ''
        for i in range(0, spacing):
            tabStr += '\t'
        self.print(f'{tabStr}{self.name}', module.filepath)
        for k, leaf in self.leafs.items():
            leaf.print_map(spacing+1, module)
        for k, container in self.containers.items():
            container.print_map(spacing+1, module)
        for k, list_item in self.lists.items():
            list_item.print_map(spacing+1, module)

    def process_leafrefs(self, hierarchy):
        new_hierarchy = []
        new_hierarchy += hierarchy
        new_hierarchy.append(self)
        for k, v in self.containers.items():
            v.process_leafrefs(new_hierarchy)
        for k, v in self.lists.items():
            v.process_leafrefs(new_hierarchy)
        for k, v in self.leafs.items():
            v.process_leafrefs(new_hierarchy)


class List(PIXIBase):

    def __init__(self, list_data):
        self.name = list_data['@name']
        self.description = list_data['description']['text'] if 'description' in list_data else None
        self.key = list_data['key']['@value'] if 'key' in list_data else None
        self.config = False if 'config' in list_data and list_data['config']['@value'] == "false" else True
        self.containers = {}
        self.lists = {}
        self.leafs = {}
        self.supported = True
        self.namespace = None
    
    def add_container(self, container_data):
        self.containers[container_data['@name']] = Container(container_data)
        return self.containers[container_data['@name']]

    def add_list(self, list_data):
        self.lists[list_data['@name']] = List(list_data)
        return self.lists[list_data['@name']]

    def add_leaf(self, leaf_data, type, isList):
        self.leafs[leaf_data['@name']] = Leaf(leaf_data, type, isList)

    def print_map(self, spacing, module):
        tabStr = ''
        for i in range(0, spacing):
            tabStr += '\t'
        self.print(f'{tabStr}{self.name}', module.filepath)
        for k, leaf in self.leafs.items():
            leaf.print_map(spacing+1, module)
        for k, container in self.containers.items():
            container.print_map(spacing+1, module)
        for k, list_item in self.lists.items():
            list_item.print_map(spacing+1, module)

    def process_leafrefs(self, hierarchy):
        new_hierarchy = []
        new_hierarchy += hierarchy
        new_hierarchy.append(self)
        for k, v in self.containers.items():
            v.process_leafrefs(new_hierarchy)
        for k, v in self.lists.items():
            v.process_leafrefs(new_hierarchy)
        for k, v in self.leafs.items():
            v.process_leafrefs(new_hierarchy)


class Leaf(PIXIBase):

    def __init__(self, leaf_data, type_data, isList):
        self.name = leaf_data['@name']
        self.description = leaf_data['description']['text'] if 'description' in leaf_data else None
        self.type = type_data
        self.isList = isList
        self.mandatory = True if 'mandatory' in leaf_data and leaf_data['mandatory']['@value'] == "true" else False
        self.config = False if 'config' in leaf_data and leaf_data['config']['@value'] == "false" else True
        if 'default' in leaf_data:
            val = leaf_data['default']['@value']
            if type_data['ptype'] == 'int':
                val = int(val)
            elif type_data['ptype'] == 'bool':
                val = True if val == 'true' else False
            self.default_value = val
        else:
            if type_data['ptype'] == 'int':
                self.default_value = 0
            elif type_data['ptype'] == 'bool':
                self.default_value = False
            else:
                self.default_value = ''
        self.when = leaf_data['when']['@condition'] if 'when' in leaf_data else None
        self.supported = True
        self.namespace = None

    def print_map(self, spacing, module):
        if self.supported:
            tabStr = ''
            for i in range(0, spacing):
                tabStr += '\t'
            if self.mandatory:
                tabStr += '+'
            if not self.config:
                tabStr += '-'
            self.print(f'{tabStr}{self.name} : {self.type["ptype"]}', module.filepath)

    def process_leafrefs(self, hierarchy):
        if 'leafref' in self.type:
            # Need to process
            if self.type['leafref'].startswith('..'):
                # Relative path
                path_list = self.type['leafref'].split('/')
                relative_index = 0
                relative = None
                for path in path_list:
                    if path == '..':
                        relative_index += 1
                    else:
                        if relative == None:
                            if relative_index < len(hierarchy):
                                relative = hierarchy[-relative_index]
                            else:
                                #TODO: external leafref support
                                #print("Warning: unable to parse external leafref")
                                return
                        if path in relative.containers:
                            relative = relative.containers[path]
                        elif path in relative.lists:
                            relative = relative.lists[path]
                        elif path in relative.leafs:
                            relative = relative.leafs[path]
                        else:
                            print("Cannot find relative path")
                            relative = None
                if relative:
                    self.type['ptype'] = relative.type['ptype']
                    if 'values' in relative.type:
                        self.type['values'] = relative.type['values']
                else:
                    print("Uhoh")
            else:
                # Absolute path
                #print([h.name for h in hierarchy])
                #print(self.name)
                #print(self.type['leafref'])
                pass
                

class Augment(PIXIBase):

    def __init__(self, augment_data):
        self.target = augment_data['@target-node']
        self.description = augment_data['description']['text'] if 'description' in augment_data else None
        self.uses = [u['@name'] for u in listify(augment_data['uses'])] if 'uses' in augment_data else None
        self.condition = augment_data['when']['@condition'] if 'when' in augment_data else None
        self.container = augment_data['container'] if 'container' in augment_data else None
        self.list = augment_data['list'] if 'list' in augment_data else None
        self.leaf = augment_data['leaf'] if 'leaf' in augment_data else None


class RPC(PIXIBase):

    def __init__(self, rpc_data):
        self.name = rpc_data['@name']
        self.description = rpc_data['description']['text']
        self.leafs = {}
        self.lists = {}
        self.cases = {}

    def add_leaf(self, leaf_data, type, isList):
        self.leafs[leaf_data['@name']] = Leaf(leaf_data, type, isList)

    def add_list(self, list_data):
        self.lists[list_data['@name']] = List(list_data)
        return self.lists[list_data['@name']]

    def add_case(self, case_data):
        self.cases[case_data['@name']] = Case(case_data)
        return self.cases[case_data['@name']]


class Case(PIXIBase):

    def __init__(self, case_data):
        self.name = case_data['@name']
        self.description = case_data['description']['text'] if 'description' in case_data else None
        self.when = case_data['when']['@condition'] if 'when' in case_data else None
        self.leafs = {}
    
    def add_leaf(self, leaf_data, type, isList):
        self.leafs[leaf_data['@name']] = Leaf(leaf_data, type, isList)

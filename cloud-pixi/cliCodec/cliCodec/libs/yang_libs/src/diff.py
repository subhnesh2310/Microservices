import os
import json
import webbrowser

from libs.yang_libs.src.parse import GXParser

class DiffParser():

    def __init__(self, from_dir, to_dir):
        self.diffs = []
        '''
        
        self.after_config = after_config
        with open(os.path.join('config', 'schema.json')) as fh:
            config = json.load(fh)
            if before_name not in config:
                raise RuntimeError(f"Target config {before_name} not supported")
            self.before_config = config[before_name]
        self.after_base_path = os.path.join('build', after_config['build'])
        self.before_base_path = os.path.join('build', self.before_config['build'])
        self.after_parser = GXParser(self.after_base_path, after_config['recipe'])
        self.after_parser.process_leafrefs()
        self.after_parser.process_identityrefs()

        self.before_parser = GXParser(self.before_base_path, self.before_config['recipe'])
        self.before_parser.process_leafrefs()
        self.before_parser.process_identityrefs()
        '''
        self.from_dir = os.path.split(from_dir)[1]
        self.to_dir = os.path.split(to_dir)[1]
        self.before_parser = GXParser(from_dir, 'infinera')
        self.before_parser.process_leafrefs()
        self.before_parser.process_identityrefs()
        self.after_parser = GXParser(to_dir, 'infinera')
        self.after_parser.process_leafrefs()
        self.after_parser.process_identityrefs()
        #self.before_parser = before_parser
        #self.after_parser = after_parser
        self.diff_it()

    def diff_it(self):
        for after_mod in self.after_parser.pixi_module_list:
            hierarchy = [after_mod]
            before_mod = [b for b in self.before_parser.pixi_module_list if after_mod.full_name == b.full_name]
            if before_mod:
                self.diff_module(hierarchy, before_mod[0], after_mod)
            else:
                self.diff_module(hierarchy, None, after_mod)
        for before_mod in self.before_parser.pixi_module_list:
            hierarchy = [before_mod]
            after_mod = [a for a in self.after_parser.pixi_module_list if before_mod.full_name == a.full_name]
            if not after_mod:
                self.diff_module(hierarchy, before_mod, None)

    def output(self):
        base_dir = os.path.join('libs', 'yang_libs')
        if 'diff' not in os.listdir(base_dir):
            os.mkdir(os.path.join(base_dir, 'diff'))
        base_dir = os.path.join('libs', 'yang_libs')
        #with open(os.path.join(base_dir, 'diff', 'report.md'), 'w') as fh:
        with open(os.path.join(base_dir, 'diff', 'report_template.html')) as fh:
            html_content = fh.read()
        diff_content = ""
        #build_name = self.after_config['build'].replace('_', '.')
        #build_name = build_name.replace('.', ' ', 1)
        #fh.write(f"# What's New in {build_name} YANG\n\n")
        # Added modules
        added_mod = [d for d in self.diffs if d.type == 'added' and d.obj_type == 'module']
        if added_mod:
            diff_content += f"<h2>New Modules</h2>\n"
            diff_content += "<ul>\n"
            for a in added_mod:
                diff_content += f"<li>{a.after.full_name}</li>\n"
            diff_content += "</ul>\n"
        # Removed modules
        removed_mod = [d for d in self.diffs if d.type == 'removed' and d.obj_type == 'module']
        if removed_mod:
            diff_content += f"<h2>Removed Modules</h2>\n"
            diff_content += "<ul>\n"
            for r in removed_mod:
                diff_content += f"<li>{r.before.full_name}</li>\n"
            diff_content += "</ul>\n"
        diff_content += f"<h2>New/Changed Elements in Existing Modules</h2>\n"
        for after_mod in self.after_parser.pixi_module_list:
            #diff_content += f"- {after_mod.full_name}\n")
            node_types = ['grouping', 'container', 'list', 'leaf']
            for node in node_types:
                ds = [d for d in self.diffs if d.module.full_name == after_mod.full_name and d.obj_type == node]
                if ds:
                    added = [a for a in ds if a.type == 'added']
                    removed = [a for a in ds if a.type == 'removed']
                    changed = [a for a in ds if a.type == 'changed' and a.obj_type != 'description']
                    if added or removed or changed:
                        diff_content += "<ul>\n"
                        diff_content += f"  <li><strong>{after_mod.full_name}</strong></li>\n"
                    if added:
                        diff_content += "  <ul>\n"
                        diff_content += f"  <li>New Elements:</li>\n"
                        diff_content += "    <ul>\n"
                        for a in added:
                            xpath = ".".join(a.xpath.split('.')[1:])
                            diff_content += f"    <li>{xpath}</li>\n"
                            diff_content += "      <ul>\n"
                            if node != 'grouping' and a.after.description:
                                diff_content += f"      <li>{a.after.description}</li>\n"
                            if node == 'leaf':
                                diff_content += f"      <li>Type: {a.after.type['ptype']}</li>\n"
                                if 'values' in a.after.type:
                                    diff_content += "        <ul>\n"
                                    diff_content += f"          <li>Values: {', '.join(a.after.type['values'])}</li>\n"
                                    diff_content += "        </ul>\n"
                            diff_content += "      </ul>\n"
                        diff_content += "    </ul>\n"
                    if removed:
                        diff_content += "  <ul>\n"
                        diff_content += f"<li>Removed Elements:</li>\n"
                        diff_content += "    <ul>\n"
                        for r in removed:
                            xpath = ".".join(r.xpath.split('.')[1:])
                            diff_content += f"    <li>{xpath}</li>\n"
                            diff_content += f"      <ul>\n"
                            if node != 'grouping' and r.before.description:
                                diff_content += f"      <li>{r.before.description}</li>\n"
                            if node == 'leaf':
                                diff_content += f"      <li>Type: {r.before.type['ptype']}</li>\n"
                                if 'values' in r.before.type:
                                    diff_content += "        <ul>\n"
                                    diff_content += f"          <li>Values: {', '.join(r.before.type['values'])}</li>\n"
                                    diff_content += "        </ul>\n"
                            diff_content += f"      </ul>\n"
                        diff_content += "    </ul>\n"
                    if changed:
                        diff_content += "  <ul>\n"
                        diff_content += f"<li>Changed Elements:</li>\n"
                        diff_content += "    <ul>\n"
                        for c in changed:
                            xpath = ".".join(xpath.split('.')[1:])
                            if node != 'grouping' and c.after.description:
                                diff_content += f"      <li>{c.after.description}</li>\n"
                            diff_content += f"      <li>{c.xpath}: {c.obj_type}</li>\n"
                            diff_content += f"      <li>{c.before} -> {c.after}</li>\n"
                            diff_content += f"      </ul>\n"
                        diff_content += "    </ul>\n"
                    if added or removed or changed:
                        diff_content += "  </ul>\n"
                        diff_content += "</ul>\n"
        html_content = html_content.replace("{{content_template}}", diff_content)
        output_file = os.path.join(base_dir, 'diff', f'report_{self.from_dir}_{self.to_dir}.html')
        with open(output_file, 'w') as fh:
            fh.write(html_content)
        webbrowser.open(output_file)

    def check_test_list(self, test_list):
        ds = [d for d in self.diffs if d.type == 'removed' and d.obj_type == 'leaf']
        arg_names = [a.before.name for a in ds]
        print(arg_names)
        for k, v in test_list.items():
            if v.get('Code'):
                check_list = [a for a in arg_names if a in v['Code']]
                if check_list:
                    print(f"Args found!: {check_list}")

    def diff_module(self, hierarchy, before_mod, after_mod):
        xpath = self.to_xpath(hierarchy)
        if not before_mod:
            self.add_diff('added', 'module', hierarchy, before_mod, after_mod)
            #print(f"Added module: {xpath}")
        elif not after_mod:
            self.add_diff('removed', 'module', hierarchy, before_mod, after_mod)
            #print(f"Removed module: {xpath}")
        else:
            for g_name, g_data in after_mod.groupings.items():
                new_hierarchy = hierarchy + [g_data]
                before_g = before_mod.groupings.get(g_name, {})
                if before_g:
                    self.diff_grouping(new_hierarchy, before_g, g_data)
                else:
                    self.diff_grouping(new_hierarchy, None, g_data)
            for g_name, g_data in before_mod.groupings.items():
                new_hierarchy = hierarchy + [g_data]
                if g_name not in after_mod.groupings:
                    self.diff_grouping(new_hierarchy, g_data, None)
            # Containers
            self.diff_all_containers(hierarchy, before_mod, after_mod)
            # Lists
            self.diff_all_lists(hierarchy, before_mod, after_mod)

    def diff_grouping(self, hierarchy, before_group, after_group):
        xpath = self.to_xpath(hierarchy)
        if not before_group:
            self.add_diff('added', 'grouping', hierarchy, before_group, after_group)
            #print(f"Added grouping: {xpath}")
        elif not after_group:
            self.add_diff('removed', 'grouping', hierarchy, before_group, after_group)
            #print(f"Removed grouping: {xpath}")
        else:
            #print(f"Diffing: {before_group.name} : {after_group.name}")
            # Containers
            self.diff_all_containers(hierarchy, before_group, after_group)
            # Lists
            self.diff_all_lists(hierarchy, before_group, after_group)
            # Leafs
            self.diff_all_leafs(hierarchy, before_group, after_group)

    def diff_all_containers(self, hierarchy, before_obj, after_obj):
        for c_name, c_data in after_obj.containers.items():
            new_hierarchy = hierarchy + [c_data]
            before_c = before_obj.containers.get(c_name, {})
            if before_c:
                self.diff_container(new_hierarchy, before_c, c_data)
            else:
                self.diff_container(new_hierarchy, None, c_data)
        for c_name, c_data in before_obj.containers.items():
            new_hierarchy = hierarchy + [c_data]
            if c_name not in after_obj.containers:
                self.diff_container(new_hierarchy, c_data, None)

    def diff_all_lists(self, hierarchy, before_obj, after_obj):
        for l_name, l_data in after_obj.lists.items():
            new_hierarchy = hierarchy + [l_data]
            before_l = before_obj.lists.get(l_name, {})
            if before_l:
                self.diff_list(new_hierarchy, before_l, l_data)
            else:
                self.diff_list(new_hierarchy, None, l_data)
        for l_name, l_data in before_obj.lists.items():
            new_hierarchy = hierarchy + [l_data]
            if l_name not in after_obj.lists:
                self.diff_list(new_hierarchy, l_data, None)

    def diff_all_leafs(self, hierarchy, before_obj, after_obj):
        for l_name, l_data in after_obj.leafs.items():
            new_hierarchy = hierarchy + [l_data]
            before_l = before_obj.leafs.get(l_name, {})
            if before_l:
                self.diff_leaf(new_hierarchy, before_l, l_data)
            else:
                self.diff_leaf(new_hierarchy, None, l_data)
        for l_name, l_data in before_obj.leafs.items():
            new_hierarchy = hierarchy + [l_data]
            if l_name not in after_obj.leafs:
                self.diff_leaf(new_hierarchy, l_data, None)

    def diff_container(self, hierarchy, before_con, after_con):
        xpath = self.to_xpath(hierarchy)
        if not before_con:
            self.add_diff('added', 'container', hierarchy, before_con, after_con)
            #print(f"Added container: {xpath}")
        elif not after_con:
            self.add_diff('removed', 'container', hierarchy, before_con, after_con)
            #print(f"Removed container: {xpath}")
        else:
            #print(f"Diffing: {before_con.name} : {after_con.name}")
            # Containers
            self.diff_all_containers(hierarchy, before_con, after_con)
            # Lists
            self.diff_all_lists(hierarchy, before_con, after_con)
            # Leafs
            self.diff_all_leafs(hierarchy, before_con, after_con)

    def diff_list(self, hierarchy, before_list, after_list):
        xpath = self.to_xpath(hierarchy)
        if not before_list:
            self.add_diff('added', 'list', hierarchy, before_list, after_list)
            #print(f"Added list: {xpath}")
        elif not after_list:
            self.add_diff('removed', 'list', hierarchy, before_list, after_list)
            #print(f"Removed list: {xpath}")
        else:
            #print(f"Diffing: {before_list.name} : {after_list.name}")
            # Containers
            self.diff_all_containers(hierarchy, before_list, after_list)
            # Lists
            self.diff_all_lists(hierarchy, before_list, after_list)
            # Leafs
            self.diff_all_leafs(hierarchy, before_list, after_list)

    def diff_leaf(self, hierarchy, before_leaf, after_leaf):
        xpath = self.to_xpath(hierarchy)
        if not before_leaf:
            self.add_diff('added', 'leaf', hierarchy, before_leaf, after_leaf)
            #print(f"Added leaf: {xpath}")
        elif not after_leaf:
            self.add_diff('removed', 'leaf', hierarchy, before_leaf, after_leaf)
            #print(f"Removed leaf: {xpath}")
        else:
            self.diff_element(hierarchy, 'ptype', before_leaf.type['ptype'], after_leaf.type['ptype'])
            if 'values' in before_leaf.type:
                self.diff_element(hierarchy, 'values', before_leaf.type['values'], after_leaf.type['values'])
            self.diff_element(hierarchy, 'description', before_leaf.description, after_leaf.description)
            self.diff_element(hierarchy, 'config', before_leaf.config, after_leaf.config)
            self.diff_element(hierarchy, 'default_value', before_leaf.default_value, after_leaf.default_value)

    def diff_type(self, hierarchy, before_leaf, after_leaf):
        xpath = self.to_xpath(hierarchy)
        self.diff_element(hierarchy, before_leaf['ptype'], after_leaf['ptype'])

    def diff_element(self, hierarchy, obj_type, before_elem, after_elem):
        xpath = self.to_xpath(hierarchy)
        if isinstance(before_elem, list):
            removed = [b for b in before_elem if b not in after_elem]
            added = [a for a in after_elem if a not in before_elem]
            if removed:
                self.add_diff('removed', obj_type, hierarchy, before_elem, after_elem)
                #print(f"Removed values for {xpath}: {removed}")
            if added:
                self.add_diff('added', obj_type, hierarchy, before_elem, after_elem)
                #print(f"Added values for {xpath}: {added}")
        else:
            if before_elem != after_elem:
                self.add_diff('changed', obj_type, hierarchy, before_elem, after_elem)
                #print(f"Diff for {xpath}: {before_elem} -> {after_elem}")

    def add_diff(self, diff_type, obj_type, hierarchy, before_content, after_content):
        self.diffs.append(Diff(diff_type, obj_type, hierarchy, before_content, after_content))

    @staticmethod
    def to_xpath(hierarchy):
        return ".".join([o.name for o in hierarchy])


class Diff():

    def __init__(self, diff_type, obj_type, hierarchy, before_content, after_content):
        self.type = diff_type
        self.obj_type = obj_type
        self.hierarchy = hierarchy
        self.xpath = ".".join([h.name for h in hierarchy])
        self.module = hierarchy[0]
        self.before = before_content
        self.after = after_content


class DiffGenerator():

    diffs = dict()
    def __init__(self, source_config, before_name):
        self.after_config = source_config
        with open(os.path.join('config', 'schema.json')) as fh:
            config = json.load(fh)
            if before_name not in config:
                raise RuntimeError(f"Target config {before_name} not supported")
            self.before_config = config[before_name]
        after_base_path = os.path.join('build', source_config['build'])
        before_base_path = os.path.join('build', self.before_config['build'])

        self.after_data = dict()
        self.before_data = dict()
        before_files = os.listdir(os.path.join(before_base_path, 'output'))
        for out_json in os.listdir(os.path.join(after_base_path, 'output')):
            with open(os.path.join(after_base_path, 'output', out_json)) as fh:
                self.after_data[out_json] = json.load(fh)
            if out_json in before_files:
                with open(os.path.join(before_base_path, 'output', out_json)) as fh:
                    self.before_data[out_json] = json.load(fh)
        self.diff_it()
        self.generate_report()
        
    def add_diff(self, name, xpath, after, before):
        xbits = xpath.split('/')
        obj = xbits[1]
        mod_xpath = "/".join(xbits[2:])
        #print(f"Diff for {name}-- Before: {after}, After: {before}")
        if obj not in self.diffs:
            self.diffs[obj] = {"added": list(), "removed": list(), "changed": list()}
        if after and before:
            self.diffs[obj]['changed'].append({"xpath": mod_xpath, "attr": name, "new": after, "old": before})
        elif after and not before:
            self.diffs[obj]['added'].append({"xpath": mod_xpath, "attr": name, "add": after})
        elif not after and before:
            self.diffs[obj]['removed'].append({"xpath": mod_xpath, "attr": name, "remove": before})

    def generate_report(self):
        for k, v in self.diffs.items():
            print(f"Diff for {k}:")
            if len(v['added']) > 0:
                print("Added:")
                for i in v['added']:
                    print(f"    xpath: {i['xpath']}")
                    print(f"    attr: {i['attr']}")
                    print(f"    value: {i['add']}")
            if len(v['removed']) > 0:
                print("Removed:")
                for i in v['removed']:
                    print(f"    xpath: {i['xpath']}")
                    print(f"    attr: {i['attr']}")
                    print(f"    value: {i['remove']}")
            if len(v['changed']) > 0:
                print("Changed:")
                for i in v['changed']:
                    print(f"    xpath: {i['xpath']}")
                    print(f"    attr: {i['attr']}")
                    print(f"    old: {i['old']}")
                    print(f"    new: {i['new']}")
    
    def diff_it(self):
        def diff_dict(after, before, xpath):
            for k, v in after.items():
                #print(k)
                if isinstance(v, dict):
                    if 'type' in v and 'ptype' in v['type']:
                        # This is an arg
                        if k in before:
                            # Arg in both
                            diff_args(v, before[k], f"{xpath}/{k}")
                        else:
                            # Arg only in after
                            self.add_diff(k, f"{xpath}/{k}", v, None)
                    elif k in before:
                        diff_dict(v, before[k], f"{xpath}/{k}")
                    else:
                        # Key in after, not in before
                        self.add_diff(k, f"{xpath}/{k}", v, None)
                elif isinstance(v, list):
                    if k in before:
                        diff_dict(v[0], before[k][0], f"{xpath}/{k}")
                    else:
                        self.add_diff(k, f"{xpath}/{k}", v, None)
            for k, v in before.items():
                if k not in after:
                    # Key not in after, in before
                    self.add_diff(k, f"{xpath}/{k}", None, before[k])
        def diff_args(after_arg, before_arg, xpath):
            for k, v in after_arg.items():
                if k == 'type':
                    pass
                else:
                    if after_arg[k] == before_arg[k]:
                        #print("No diff")
                        pass
                    else:
                        self.add_diff(k, xpath, after_arg[k], before_arg[k])
        diff_dict(self.after_data, self.before_data, "")

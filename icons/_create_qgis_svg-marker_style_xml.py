import glob
import base64
st_xml = '<!DOCTYPE qgis_style>\n'
st_xml += '<qgis_style version="2">\n'
st_xml += '  <symbols>\n'
for file in glob.glob('./*.svg'):
     with open(file, 'r') as f:
         st_name = f.name
         file_name = st_name.split('/')[1]
         big_name = file_name.split('.')[0]
         title_name = big_name.title() 
         original_svg = f.read()
         byte_svg = original_svg.encode('ascii')
         b64_bytes = base64.b64encode(byte_svg)
         base64_svg = b64_bytes.decode('ascii')
         f.close()
         st_xml += '    <symbol name="' + title_name + '" force_rhr="0" tags="Temaki" clip_to_extent="1" type="marker" alpha="1">\n'
         st_xml += '      <data_defined_properties>\n'
         st_xml += '        <Option type="Map">\n'
         st_xml += '          <Option value="" name="name" type="QString"/>\n'
         st_xml += '          <Option name="properties"/>\n'
         st_xml += '          <Option value="collection" name="type" type="QString"/>\n'
         st_xml += '        </Option>\n'
         st_xml += '      </data_defined_properties>\n'
         st_xml += '      <layer locked="0" pass="0" enabled="1" class="SvgMarker">\n'
         st_xml += '        <Option type="Map">\n'
         st_xml += '          <Option value="0" name="angle" type="QString"/>\n'
         st_xml += '          <Option value="0,0,0,255" name="color" type="QString"/>\n'
         st_xml += '          <Option value="0" name="fixedAspectRatio" type="QString"/>\n'
         st_xml += '          <Option value="1" name="horizontal_anchor_point" type="QString"/>\n'
         st_xml += '          <Option value="base64:' + base64_svg + '" name="name" type="QString"/>'
         st_xml += '          <Option value="0,0" name="offset" type="QString"/>\n'
         st_xml += '          <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>\n'
         st_xml += '          <Option value="MM" name="offset_unit" type="QString"/>\n'
         st_xml += '          <Option value="255,255,255,255" name="outline_color" type="QString"/>\n'
         st_xml += '          <Option value="0" name="outline_width" type="QString"/>\n'
         st_xml += '          <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>\n'
         st_xml += '          <Option value="MM" name="outline_width_unit" type="QString"/>\n'
         st_xml += '          <Option name="parameters"/>\n'
         st_xml += '          <Option value="diameter" name="scale_method" type="QString"/>\n'
         st_xml += '          <Option value="7" name="size" type="QString"/>\n'
         st_xml += '          <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>\n'
         st_xml += '          <Option value="MM" name="size_unit" type="QString"/>\n'
         st_xml += '          <Option value="1" name="vertical_anchor_point" type="QString"/>\n'
         st_xml += '        </Option>\n'
         st_xml += '        <prop k="angle" v="0"/>\n'
         st_xml += '        <prop k="color" v="0,0,0,255"/>\n'
         st_xml += '        <prop k="fixedAspectRatio" v="0"/>\n'
         st_xml += '        <prop k="horizontal_anchor_point" v="1"/>\n'
         st_xml += '        <prop k="name" v="base64:' + base64_svg + '"/>\n'
         st_xml += '        <prop k="offset" v="0,0"/>\n'
         st_xml += '        <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>\n'
         st_xml += '        <prop k="offset_unit" v="MM"/>\n'
         st_xml += '        <prop k="outline_color" v="255,255,255,255"/>\n'
         st_xml += '        <prop k="outline_width" v="0"/>\n'
         st_xml += '        <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>\n'
         st_xml += '        <prop k="outline_width_unit" v="MM"/>\n'
         st_xml += '        <prop k="parameters" v=""/>\n'
         st_xml += '        <prop k="scale_method" v="diameter"/>\n'
         st_xml += '        <prop k="size" v="7"/>\n'
         st_xml += '        <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>\n'
         st_xml += '        <prop k="size_unit" v="MM"/>\n'
         st_xml += '        <prop k="vertical_anchor_point" v="1"/>\n'
         st_xml += '        <data_defined_properties>\n'
         st_xml += '          <Option type="Map">\n'
         st_xml += '            <Option value="" name="name" type="QString"/>\n'
         st_xml += '            <Option name="properties"/>\n'
         st_xml += '            <Option value="collection" name="type" type="QString"/>\n'
         st_xml += '          </Option>\n'
         st_xml += '        </data_defined_properties>\n'
         st_xml += '      </layer>\n'
         st_xml += '    </symbol>\n'

st_xml += '  </symbols>\n'
st_xml += '  <colorramps/>\n'
st_xml += '  <textformats/>\n'
st_xml += '  <labelsettings/>\n'
st_xml += '  <legendpatchshapes/>\n'
st_xml += '  <symbols3d/>\n'
st_xml += '</qgis_style>\n'

target = open('temaki.xml', 'w')
target.write(st_xml)
target.close()

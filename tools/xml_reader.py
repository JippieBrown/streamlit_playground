import xmltodict



def xml_reader(file):
	try:
		content = xmltodict.parse(file.read())#.encode("cp1252"))
	except:
		pass
	return content



# # with open(xml_file) as fd:
# # 		doc = xmltodict.parse(fd.read().encode("cp1252"))

# if 'form1' in list(doc.keys()):
# # Set variable
# 	item = doc['form1']

# # yes no dropdown elements
# 	if 'Block1'				  in list(item.keys()):			
# 		if 'Bauleiter'		   in list(item['Block1'].keys()):		read_xml.supervision			  = item['Block1']['Bauleiter']					   
# 		if 'IBSler'			  in list(item['Block1'].keys()):		read_xml.commissioning			= item['Block1']['IBSler']						  
# 		if 'MPD_2'			   in list(item['Block1'].keys()):		read_xml.mpd					  = item['Block1']['MPD_2']  
# 	if 'Block2'				  in list(item.keys()): 
# 		if 'Werkzeug_2'		  in list(item['Block2'].keys()):		read_xml.tools					= item['Block2']['Werkzeug_2']					  
# 		if 'HV'				  in list(item['Block2'].keys()):		read_xml.hv_test_equipment		= item['Block2']['HV-Test_2']  
# 	if 'Block3'				  in list(item.keys()): 
# 		if 'Transport_2'		 in list(item['Block3'].keys()):		read_xml.transport				= item['Block3']['Transport_2']  
# 	if 'Block4'				  in list(item.keys()): 
# 		if 'Erdung_2'			in list(item['Block4'].keys()):		read_xml.earthing				 = item['Block4']['Erdung_2'] 
# 	if 'Block5'				  in list(item.keys()): 
# 		if 'PSD2'				in list(item['Block5'].keys()):		read_xml.psd					  = item['Block5']['PSD2']							
# 		if 'LIBO_2'			  in list(item['Block5'].keys()):		read_xml.libo					 = item['Block5']['LIBO_2']						  
# 		if 'Training_2'		  in list(item['Block5'].keys()):		read_xml.customer_training		= item['Block5']['Training_2']	
# 	if 'Block6'				  in list(item.keys()):		
# 		if 'Hallenkran_2'		in list(item['Block6'].keys()):		read_xml.indoor_crane			 = item['Block6']['Hallenkran_2']					
# 		if 'DC_versorgung_2'	 in list(item['Block6'].keys()):		read_xml.dc_supply				= item['Block6']['DC_versorgung_2']				 
		
# # drop down elements
# 	if 'Anlagentyp'			  in list(item.keys()):				  read_xml.plant_type			   = item['Anlagentyp']							   
# 	if 'Gueltigkeit'			 in list(item.keys()):				  read_xml.validity				 = item['Gueltigkeit']							   
# 	if 'Schutzkl_1'			  in list(item.keys()):				  read_xml.protection_class_indoor  = item['Schutzkl_1']								
# 	if 'Schutzkl_2'			  in list(item.keys()):				  read_xml.protection_class_outdoor = item['Schutzkl_2']								
# 	if 'Angebot'				 in list(item.keys()):				  read_xml.calc_for				 = item['Angebot']								   
# 	if 'SaS'					 in list(item.keys()):				  read_xml.busbar				   = item['SaS']									   
# 	if 'Block1'				  in list(item.keys()):
# 		if 'DropDownlist11'	  in list(item['Block1'].keys()):		read_xml.language				 = item['Block1']['DropDownlist11']				  
# 	if 'Block4'				  in list(item.keys()):
# 		if 'Sekundaer_2'		 in list(item['Block4'].keys()):		read_xml.sec_works				= item['Block4']['Sekundaer_2']					 
# 	if 'Block5'				  in list(item.keys()):
# 		if 'DropDownList28'	  in list(item['Block5'].keys()):		read_xml.pd_measurement		   = item['Block5']['DropDownList28']				  
# 	if 'Block5'				  in list(item.keys()):
# 		if 'ACTAS2'			  in list(item['Block5'].keys()):		read_xml.actas					= item['Block5']['ACTAS2']						  
# 	if 'Block6'				  in list(item.keys()):
# 		if 'HS_Kabel_2'		  in list(item['Block6'].keys()):		read_xml.hv_plugs				 = item['Block6']['HS_Kabel_2']				 
# 	if 'Block6'				  in list(item.keys()):
# 		if 'Kabelsteckbuchsen'   in list(item['Block6'].keys()):		read_xml.hv_plug_size			 = item['Block6']['Kabelsteckbuchsen']		  
	
# # Freetext
# 	if 'Vorname'				 in list(item.keys()):				  read_xml.first_name			   = item['Vorname']								   
# 	if 'Nachname'				in list(item.keys()):				  read_xml.last_name				= item['Nachname']								  
# 	if 'Abteilung'			   in list(item.keys()):				  read_xml.department			   = item['Abteilung']								 
# 	if 'ProjektName'			 in list(item.keys()):				  read_xml.project_name			 = item['ProjektName']							   
# 	if 'Projektland'			 in list(item.keys()):				  read_xml.country				  = item['Projektland']							   
# 	if 'TextField5'			  in list(item.keys()):				  read_xml.city					 = item['TextField5']								 
# 	if 'Block6'				  in list(item.keys()):				  
# 		if 'Bemerkung'		   in list(item['Block6'].keys()):		read_xml.remark				   = item['Block6']['Bemerkung']					   
# 	if 'Anzahl'				  in list(item.keys()):				  read_xml.number_of_bays		   = item['Anzahl']									
# 	if 'Block4'				  in list(item.keys()):					
# 		if 'Felder_Zahl1'		in list(item['Block4'].keys()):		read_xml.sec_works_no_of_bays	 = item['Block4']['Felder_Zahl1']			   

# # Dates
# 	if 'DateField1'			  in list(item.keys()):				  read_xml.inquiry_date			 = item['DateField1']									   
# 	if 'Block6'				  in list(item.keys()):
# 		if 'DateField2'		  in list(item['Block6'].keys()):		read_xml.offer_until			  = item['Block6']['DateField2']						 
# 	if 'Block6'				  in list(item.keys()):
# 		if 'DateField3'		  in list(item['Block6'].keys()):		read_xml.kick_off_meeting		 = item['Block6']['DateField2']													
# 	#read_xml.date_of_editing		  = datetime.today()								

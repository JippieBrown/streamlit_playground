import streamlit as st
import ldap

# import win32com.client
# import pythoncom

def ECDReader(Selector):
	l = ldap.initialize('LDAP://ad101.siemens-energy.net:3268')
	Fields = "sAMAccountName,otherPager,c,Manager,siemens-costLocationUnit,siemens-costLocation,mobile,physicalDeliveryOfficeName,msDS-PhoneticFirstName,sn,Title,Department,siemens-gid,mail, postalcode, l, streetaddress, company"
	query = "SELECT " + Fields + " FROM 'LDAP://ad101.siemens-energy.net:3268/DC=ad101,DC=siemens-energy,DC=net' WHERE mail='" + Selector + "'"
	l.set_option(ldap.OPT_REFERRALS, 0)
	l.simple_bind_s('haukemaier@siemens-energy.com', '!')
	result = l.search_s('LDAP://ad101.siemens-energy.net:3268/DC=ad101,DC=siemens-energy,DC=net',
                          ldap.SCOPE_SUBTREE,
                          'mail=haukemaier@siemens-emergy.com',
                          ['mobile'])
	'''
	The Selector is the email address of the person, who is searched for. all_dict shows all requested values (if toggle comment)

	Relevant fields:
	- 'company'
	- 'street'
	- 'city'
	- 'postal_code'
	- 'email'
	- 'gid'
	- 'department'
	- 'last_name'
	- 'first_name'
	- 'office'
	- 'mobile'
	- 'country'
	'''
	
	# pythoncom.CoInitialize()
	Fields = "sAMAccountName,otherPager,c,Manager,siemens-costLocationUnit,siemens-costLocation,mobile,physicalDeliveryOfficeName,msDS-PhoneticFirstName,sn,Title,Department,siemens-gid,mail, postalcode, l, streetaddress, company"
	query = "SELECT " + Fields + " FROM 'LDAP://ad101.siemens-energy.net:3268/DC=ad101,DC=siemens-energy,DC=net' WHERE mail='" + Selector + "'"
	# adoConn = win32com.client.Dispatch('ADODB.Connection')
	# adoConn.Provider="ADSDSOObject"
	# adoConn.Open('ADs Provider')
	# (adoRS, success) = adoConn.Execute(query)

	# fields_dict = {}
	# fields_dict['company']	  = adoRS.Fields.Item(0).Value
	# fields_dict['street']	   = adoRS.Fields.Item(1).Value
	# fields_dict['city']		 = adoRS.Fields.Item(2).Value
	# fields_dict['postal_code']  = adoRS.Fields.Item(3).Value	
	# fields_dict['email']		= adoRS.Fields.Item(4).Value
	# fields_dict['gid']		  = "-"#adoRS.Fields.Item(5).Value
	# fields_dict['department']   = adoRS.Fields.Item(6).Value
	# fields_dict['last_name']	= adoRS.Fields.Item(8).Value
	# fields_dict['first_name']   = adoRS.Fields.Item(9).Value
	# fields_dict['office']	   = adoRS.Fields.Item(10).Value	
	# fields_dict['mobile']	   = adoRS.Fields.Item(11).Value
	# fields_dict['country']	  = adoRS.Fields.Item(15).Value

	# # all_dict={}
	# # for x in range(adoRS.Fields.Count):
	# #	 all_dict[x] = adoRS.Fields.Item(x).Value
	# # print(all_dict)

	# pythoncom.CoUninitialize()
	return result#fields_dict

col1, col2, col3 = st.columns([1,2,1])

col1.markdown(ECDReader("haukemaier@siemens-energy.com"))

col2.markdown("HelloHelloHelloHelloHelloHello")



col3.markdown("Hello")
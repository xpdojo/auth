# pip install python3-ldap
import ldap3

# LDAP 서버 정보
ldap_host = 'localhost'
ldap_port = 389
ldap_user_dn = 'cn=admin,dc=srv,dc=world'
ldap_password = 'admin'

# LDAP 서버 연결 설정
server = ldap3.Server(ldap_host, port=ldap_port, use_ssl=False, get_info=ldap3.ALL)
conn = ldap3.Connection(server, user=ldap_user_dn, password=ldap_password, auto_bind=True)

# ldap_search_base = 'ou=users,dc=srv,dc=world'
ldap_search_base = 'ou=people,dc=srv,dc=world'
ldap_search_filter = '(objectClass=inetOrgPerson)'

# 사용자 목록 검색
conn.search(search_base=ldap_search_base, search_filter=ldap_search_filter)

# 검색 결과 출력
for entry in conn.entries:
    print(entry)

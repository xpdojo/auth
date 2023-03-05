# LDAP

LDAP (Lightweight Directory Access Protocol)는 디렉터리 서비스를 제공하는 프로토콜입니다.
디렉터리 서비스란, 조직 내의 사용자, 그룹, 장비, 서비스 등과 같은 정보를 관리하는 시스템입니다.
LDAP 서버를 구축하여 이러한 정보를 관리하고 검색할 수 있습니다.

## OpenLDAP 패키지 설치

OpenLDAP은 LDAP 서버를 구축하기 위한 오픈 소스 소프트웨어 패키지입니다.
우분투에서는 다음 명령어를 사용하여 OpenLDAP 패키지를 설치할 수 있습니다.

```sh
apt install slapd ldap-utils
```

## 관리자 계정 설정

OpenLDAP 서버를 구축하면 기본적으로 관리자 계정이 생성됩니다.
이 계정은 모든 LDAP 객체에 대한 권한을 가집니다.
다음 명령어를 사용하여 관리자 계정을 설정합니다.

```sh
sudo dpkg-reconfigure slapd
```

명령어를 실행하면 다음과 같은 설정 창이 나타납니다.

```sh
┌───────────────────────┤ Configuring slapd ├───────────────────────┐
│ Please enter the following information:                           │
│                                                                   │
│ Omit OpenLDAP server configuration?                               │
│   No                                                              │
│                                                                   │
│ DNS domain name:                                                  │
│                                                                   │
│ Organization name:                                                │
│                                                                   │
│ Administrator password:                                           │
│                                                                   │
│ Confirm password:                                                 │
│                                                                   │
│ Database backend to use:                                          │
│   HDB - Sleepycat's Highly Available Embedded Database (BDB)      │
│   MDB - OpenLDAP's own Memory-mapped DB                           │
│                                                                   │
│ Do you want the database to be removed when slapd is purged?      │
│   Yes, remove the database when slapd is purged.                  |
│   No, I want to manually remove the database using db_destroy.    │
│                                                                   │
│ Move old database?                                                │
│   Yes, move the old database.                                     │
│   No, I will remove the old database later.                       │
│                                                                   │
│ Allow LDAPv2 protocol?                                            │
│   Yes, allow LDAPv2 protocol.                                     │
│   No, disallow LDAPv2 protocol.                                   │
│                                                                   │
│                                                            <Ok>   │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

- DNS domain name: LDAP 디렉터리의 기본 도메인 이름을 입력합니다.
  - srv.world
- Organization name: 조직 이름을 입력합니다.
  - srv.world
- Administrator password: 관리자 계정의 비밀번호를 입력합니다.
  - Confirm password: 비밀번호를 다시 한 번 입력합니다.
- Database backend to use: 사용할 데이터베이스 백엔드를 선택합니다.
- Do you want the database to be removed when slapd is purged?: slapd가 제거될 때 데이터베이스를 제거
  - No
- Move old database?
  - Yes

```sh
Backing up /etc/ldap/slapd.d in /var/backups/slapd-2.5.13+dfsg-0ubuntu0.22.04.1... done.
Moving old database directory to /var/backups:
```

## 설정 파일

```sh
sudo slapcat
```

```ldif
dn: dc=srv,dc=world
objectClass: top
objectClass: dcObject
objectClass: organization
o: srv.world
dc: srv
structuralObjectClass: organization
entryUUID: a04fa032-4f74-103d-9ec5-416050c12451
creatorsName: cn=admin,dc=srv,dc=world
createTimestamp: 20230305073937Z
entryCSN: 20230305073937.872317Z#000000#000#000000
modifiersName: cn=admin,dc=srv,dc=world
modifyTimestamp: 20230305073937Z
```

```sh
ldapadd -x -D cn=admin,dc=srv,dc=world -W -f base.ldif
```

```sh
Enter LDAP Password: <admin_password>
adding new entry "ou=people,dc=srv,dc=world"

adding new entry "ou=groups,dc=srv,dc=world"
```

## phpLDAPadmin

phpLDAPadmin은 웹 브라우저를 통해 LDAP 서버를 관리할 수 있는 웹 기반의 관리 도구입니다.
다음 명령어를 사용하여 phpLDAPadmin을 설치합니다.

```sh
apt install phpldapadmin
```

- [localhost/phpldapadmin](http://127.0.0.1/phpldapadmin/) 접속

```sh
sudo vi /etc/php/8.1/apache2/php.ini
```

```ini
; Maximum amount of memory a script may consume
; https://php.net/memory-limit
; memory_limit = 128M
memory_limit = 24
```

## 사용자 추가

```sh
slappasswd
# New password: test
# Re-enter new password: test
{SSHA}ZiyrU7ZfK7nUzJlVLS0j1RHeOC686NU/
```

```sh
ldapadd -x -D cn=admin,dc=srv,dc=world -W -f user.ldif
# Enter LDAP Password: 
# adding new entry "uid=xerus,ou=people,dc=srv,dc=world"

# adding new entry "cn=xerus,ou=groups,dc=srv,dc=world"
```

## 참고

- [OpenLDAP](https://www.openldap.org/)
- [Directory Server](https://www.server-world.info/en/note?os=Ubuntu_16.04&p=openldap&f=1) - Server World

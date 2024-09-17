from ldap3 import Server, Connection, ALL, SUBTREE
import json

# Define the LDAP server and base DN (Distinguished Name)
LDAP_SERVER = 'ldap://your_ldap_server.com'
BASE_DN = 'dc=example,dc=com'  # Adjust this according to your LDAP structure

def ldap_connect():
    try:
        # Connect to the LDAP server (anonymous bind)
        server = Server(LDAP_SERVER, get_info=ALL)
        connection = Connection(server, auto_bind=True)
        
        if connection.bind():
            print("[+] Connected to the LDAP server.")
            return connection
        else:
            print("[-] Failed to connect to the LDAP server.")
            return None
    except Exception as e:
        print(f"Error connecting to LDAP: {e}")
        return None

def search_ldap(conn):
    # Perform a search query
    search_filter = '(objectClass=*)'  # Adjust this as needed
    search_attributes = ['cn', 'sn', 'mail', 'uid']  # Adjust this as per your needs

    try:
        conn.search(BASE_DN, search_filter, search_scope=SUBTREE, attributes=search_attributes)
        
        if not conn.entries:
            print("[-] No entries found.")
            return None
        
        print(f"[+] Found {len(conn.entries)} entries.")
        return conn.entries
    except Exception as e:
        print(f"Error searching LDAP: {e}")
        return None

def parse_entries(entries):
    # Convert entries into a readable format
    parsed_data = []
    
    for entry in entries:
        parsed_entry = {}
        for attribute in entry.entry_attributes:
            parsed_entry[attribute] = entry[attribute].value
        
        parsed_data.append(parsed_entry)
    
    # Print in a readable format (JSON pretty print)
    print(json.dumps(parsed_data, indent=4))
    
    return parsed_data

def main():
    # Connect to LDAP
    conn = ldap_connect()
    if conn:
        # Search and get entries
        entries = search_ldap(conn)
        if entries:
            # Parse and display the entries
            parse_entries(entries)
        
        # Unbind connection
        conn.unbind()

if __name__ == "__main__":
    main()
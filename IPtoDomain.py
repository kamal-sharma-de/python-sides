import socket

def get_domain_name(ip_address):
  """
  Attempts to find the domain name associated with an IP address using PTR records.

  Args:
      ip_address: The IP address to lookup.

  Returns:
      The domain name associated with the IP address if found, otherwise None.
  """
  try:
    # Reverse the IP address for PTR record lookup
    hostname, aliases, addresses = socket.gethostbyaddr(ip_address)
    # Assuming the first entry in aliases is the domain name
    return aliases[0] if aliases else None
  except socket.herror:
    return None  # Handle potential DNS lookup errors

# Example usage
ip_address = "8.8.8.8"
domain_name = get_domain_name(ip_address)
print(f"Domain name for {ip_address}: {domain_name}")

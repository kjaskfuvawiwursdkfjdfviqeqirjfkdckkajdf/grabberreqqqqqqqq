import requests
import json

def fetch_domains(ip):
    url = f'https://otx.alienvault.com/otxapi/indicator/ip/passive_dns/{ip}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    domains = set()  # Use a set to avoid duplicate domains

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Extract domains from the JSON response
        for entry in data.get('passive_dns', []):
            domain = entry.get('hostname')
            if domain:
                domains.add(domain)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for IP {ip}: {e}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON response for IP {ip}.")

    return domains

def main():
    # User input for files
    ip_file = input("[+] Input file IP addressmu: ")
    output_file = input("[+] Save resultmu: ")

    with open(ip_file, 'r') as ip_list, open(output_file, 'w') as result_file:
        for ip in ip_list:
            ip = ip.strip()
            if not ip:
                continue
            print(f"\nFetching domains for IP: {ip}")
            domains = fetch_domains(ip)

            # Write only domains to the output file
            if domains:
                for domain in domains:
                    result_file.write(f"{domain}\n")
                print(f"Domains for IP {ip} saved to {output_file}")
            else:
                print(f"No domains found for IP {ip}")

    print("\nFinished processing all IPs.")

if __name__ == "__main__":
    main()

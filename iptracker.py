from ipdata import ipdata
from pprint import pprint
import time

def get_ip(api_key, ip_address):
	"""
	
	"""
	ipdata_api = ipdata.IPData(api_key)
	try:
		response = ipdata_api.lookup(ip_address)
		return response
	except Exception as e:
		print(f"Error: {e}")
		return None

def main():
	print("-----------------------------------------")
	print("Welcome to IP_Tracker")
	print("This IP_Tracker just a basic information tool to provide")
	print("IP Address information. This project use API Data from")
	print("IP Data. Please register from their website to use this script")
	print("To cancel the program use CTRL+C")
	print("Sincerly, Irzfan Farizan")
	print("Credit: Google and youtube <3")
	print("-----------------------------------------")
	time.sleep(3)
	
	#handle interrupt 
	try:

		api_key = input("Please insert your API KEY from IP Data: ")
		get_ip_user = input("Insert IP Address: ")
		ip_info = get_ip(api_key, get_ip_user)

		if ip_info:
			print("-----------------------------------------")
			print("Geolocation: ")
			print(f"IP Address: {ip_info.get('ip')}")
			print(f"Postal: {ip_info.get('postal')}")
			print(f"City: {ip_info.get('city')}")
			print(f"Region: {ip_info.get('region')}")
			print(f"Country: {ip_info.get('country_name')}")
			print(f"Latitude: {ip_info.get('latitude')}")
			print(f"Longtitude: {ip_info.get('longtitude')}")
			print("-----------------------------------------")
		else:
			print("Error to get ip information")

	except KeyboardInterrupt:
		print("\nThis program has been terminated by user.")

if __name__ == "__main__":
    main()

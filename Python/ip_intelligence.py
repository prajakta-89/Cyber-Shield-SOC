import requests


def get_ip_details(ip):

    try:

        url = f"http://ip-api.com/json/{ip}"

        response = requests.get(url, timeout=5)

        data = response.json()


        if data["status"] == "success":

            return {

                "country": data.get("country", "Unknown"),

                "city": data.get("city", "Unknown"),

                "isp": data.get("isp", "Unknown"),

                "organization": data.get("org", "Unknown")

            }


        else:

            return {

                "country": "Unknown",

                "city": "Unknown",

                "isp": "Unknown",

                "organization": "Unknown"

            }


    except Exception as e:

        print("IP Lookup Error:", e)

        return {

            "country": "Unknown",

            "city": "Unknown",

            "isp": "Unknown",

            "organization": "Unknown"

        }
from check_proxy.core.proxy_details.entities.proxy_details import ProxyDetails

def create_proxy_details(
        connection_string,
        public_ip,
        port,
        is_proxy_safe,
        proxy_type,
        country,
        isp,
        city,
        region_name,
        organization,
        lat,
        lon
    ):
    
    proxy_details = ProxyDetails()
    
    proxy_details.set_connection_string(connection_string)
    proxy_details.set_port(port)
    proxy_details.set_public_ip(public_ip)
    proxy_details.set_type(proxy_type)
    proxy_details.set_is_safe(is_proxy_safe)

    proxy_details.set_country(country)
    proxy_details.set_isp(isp)
    proxy_details.set_city(city)
    proxy_details.set_region_name(region_name)
    proxy_details.set_organization(organization)
    proxy_details.set_lat(lat)
    proxy_details.set_lon(lon)
    
    return proxy_details
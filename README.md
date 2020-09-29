# Searchoui
A tool to check the vendor of a MAC address.

# Prerequisites
* Python 3
* Requests - [Click here for library](https://github.com/psf/requests)


# Usage
```
./searchoui.py <mac address>                                                            
```

# Successful search
```
./searchoui.py F4BD9E                                                              
Cisco Systems, Inc
```
# Unsuccessful Search
```
./searchoui.py abc                                                                 
MAC address not found.
```

# Missing argument
```
./searchoui.py                                                                      
No MAC address entered.
```

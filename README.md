
# Devices and Versions Dataset

This repository is dedicated to the design and creation of a **structured dataset of network devices and their operating system versions**. The goal is to provide a useful database for cybersecurity research, vulnerability analysis, inventory automation, and the development of asset management tools.

## Purpose

The dataset aims to centralize relevant information about vendors, models, and operating system versions of network devices widely used in enterprise and telecommunications environments.

## Repository Structure

- `devices.json`: Main dataset file. Contains a list of devices, vendor (`vendor`), operating system name (`os_name`), and available versions (`os_versions`).
- `README.md`: This document.

## Dataset Format

Each entry in `devices.json` has the following structure:

```json
{
	"vendor": "<Vendor>",
	"os_name": "<Operating System Name>",
	"os_versions": ["<version1>", "<version2>", ...]
}
```

Example:

```json
{
	"vendor": "Cisco",
	"os_name": "IOS-XE",
	"os_versions": ["16.9.1", "17.3.1", "17.6.1"]
}
```

## Included Vendors and Operating Systems

Currently, the dataset includes information from:

- Cisco (ASA OS, FTD, FXOS, IOS, IOS-XE, NX-OS, IOS-XR)
- Palo Alto (PAN-OS)
- Fortinet (FortiOS)
- Juniper (Junos OS)
- Check Point (Gaia OS)
- Huawei (VRP)
- Barracuda (BarracudaOS)
- MikroTik (RouterOS)

## Contributions

Contributions are welcome! You can help in the following ways:

1. **Add new devices or versions**: Edit `devices.json` following the described format.
2. **Fix errors**: If you find incorrect information, please open an issue or submit a pull request.
3. **Suggest improvements**: Propose enhancements to the structure or scope of the dataset.

## Using the Dataset

You can use the dataset for:

- Automated network asset inventory
- Vulnerability exposure analysis
- Integration with patch management tools
- Academic or industrial research

## License

This project is distributed under the MIT license. See the LICENSE file for more details.

---
Questions or suggestions? Open an issue in this repository.

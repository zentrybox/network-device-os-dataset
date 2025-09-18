

# Devices and Versions Dataset

This repository is dedicated to the design and creation of a **structured dataset of network devices and their product versions**. The goal is to provide a useful database for cybersecurity research, vulnerability analysis, inventory automation, and the development of asset management tools.

## Purpose

The dataset centralizes relevant information about vendors, products, and their versions for network devices widely used in enterprise and telecommunications environments.

## Repository Structure

- `dataset/vendor_manifest.json`: Manifest file. Contains a list of devices with `vendor`, `product`, and `version` fields.
- `dataset/dataset.json`: Expanded dataset, generated from the manifest.
- `README.md`: This document.
- `CONTRIBUTING.md`: Contribution guidelines.
- `LICENSE`: Project license.
- `.github/`: Community health files (issue, PR templates, code of conduct).
- `docs/`: Documentation and guides.

## Manifest Format

Each entry in `vendor_manifest.json` has the following structure:

```json
{
  "vendor": "<Vendor>",
  "product": "<Product>",
  "version": ["<version1>", "<version2>", ...]
}
```

Example:

```json
{
  "vendor": "Cisco",
  "product": "ASA",
  "version": ["9.8(4)", "9.9.1"]
}
```

## Included Vendors and Products

Currently, the dataset includes information from:

- Cisco (ASA, FTD, FXOS, IOS, IOS-XE, NX-OS, IOS-XR)
- Palo Alto (PAN-OS)
- Fortinet (FortiOS)
- Juniper (Junos OS)
- Check Point (Gaia OS)
- Huawei (VRP)
- Barracuda (BarracudaOS)
- MikroTik (RouterOS)

## Contributions

Contributions are welcome! You can help in the following ways:

1. **Add new devices or versions**: Edit `vendor_manifest.json` following the described format.
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

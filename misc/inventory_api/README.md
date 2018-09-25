# Project: Inventory management webserver
*Release: 0.1*


The inventory project provides a simple API to read and write to an inventory using HTTP requests

## Features

#### This release
- [x] Get total inventory
- [x] Get the number of a specific item from inventory
- [x] Updata an item
- [x] Add an item
- [x] Delete an item
- [x] Organise the code better
- [x] Write api docs

#### Next release

- [ ] Sort by amount/


## Usage

Deploy the inventory files below to your server:

| Filename | Description |
| :-- | :-- |
| docs_Inventory.md | This file |
| environment.py | The executable wisgi server |
| inventory.py | The logic for the server |
| inventory_api.txt | The inventory itself as a json object |

### Paths

| Location | Path |
| :-- | :-- |
| Root path | `~/`|
| Inventory | `~/inventory`|
| item | `~/inventory/item`|

### HTTP request and query methods

| Method | Path | Query | Description | Examlpes |
| :-- | :-- | :-- | :-- | :-- |
| `GET` | `~/inventory/..` | na |Retrieve inventory at the current path depth | `~/inventory` gets the entire inventory, `~/inventory/pants` gets the number of pants in inventory |
| `POST` | `~/inventory/item` | `?number` | Add `int` `item`s to the inventory | `~/inventory/shorts?5` adds five shorts to the inventory |
| `PATCH` | Same as `POST` | Same as `POST` | Same as `POST` | `~/inventory/shorts?3` changes the shorts entry from above to 3 |
| `DELETE` | `~/inventory/item` | na | Deletes the `item` from the inventory | `~/inventory/shorts` deletes the shorts entry |

### Contribute


- Issue Tracker: github.com/$project/$project/issues
- Source Code: github.com/$project/$project


### Support


If you are having issues, please let me know. My email address is: r@bit.io


### License

The project is licensed under the BSD license.

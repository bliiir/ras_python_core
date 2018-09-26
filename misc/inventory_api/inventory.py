import json
import sys

class MyApp:

    """Inventory manager

    Attributes:
        filename (str): The name of the .txt file that holds the inventory json object
        fileinfo (TYPE): # The content of the inventory file as a dict object
        path (TYPE):
        bits (TYPE): A list of path elements derived from
        method (TYPE): http request - GET, POST, PATCH or DELETE
        query (TYPE): Everything after the ? character in the HTTP request
    """

    ################## BEGIN: AUX               ##################

    # Read the file from the filename
    def filereader(self):
        _dict = {}
        with open(self.filename, 'r') as f:
            _dict = json.loads(f.read())
        return _dict

    # Write the file back to the filename - replacing it
    def filewriter(self):
        json.dump(self.fileinfo, open(self.filename, 'w'))
        return "Your inventory has been updated"

    # Split the HTTP path into a list of items using the character / as the delimeter
    def get_path(self):
        return self.path.split("/")

    ################## END: AUX                 ##################


    ################## BEGIN: QUERY HANDLING    ##################

    # GET
    def _get(self):
        if self.bits[1] == "inventory":
            try: return f"{self.bits[2]}: {self.fileinfo[self.bits[2]]}"
            except: return json.dumps(self.fileinfo, indent=4)
        else: return "No inventory here"

    # POST
    def _post(self):
        # /inventory/item?number
        if self.bits[1] == "inventory":
            self.fileinfo[self.bits[2]] = self.query
            try: return self.filewriter()
            except: "Your request is invalid"

    # PATCH
    def _patch(self):
        return self._post() # Since patching is the same as replacing, I am just calling the post method

    # DELETE
    def _delete(self):
        if self.bits[1] == "inventory":
            del self.fileinfo[self.bits[2]]
            try: return self.filewriter()
            except: "Your request is invalid"

    ################## END: QUERY HANDLING      ##################


    ################## BEGIN: SETUP             ##################

    def dispatch(self, environ):
        self.filename = "inventory_api.txt"
        self.query = environ['QUERY_STRING']
        self.method = environ['REQUEST_METHOD']
        self.path = environ['PATH_INFO']
        # self.address = environ['REMOTE_ADDR']

        self.fileinfo = self.filereader() # Get the content of the inventory file as a dict object
        self.bits = self.get_path() # Get the list of path elements

        if self.method == 'GET': return(self._get())
        elif self.method == 'POST': return(self._post())
        elif self.method == 'PATCH': return(self._patch())
        elif self.method == 'DELETE': return(self._delete())
        else: "Your request is invalid, please try new URL"

    ################## END: SETUP               ##################







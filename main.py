#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2

form_html ="""
<form>
<h1>Add Food </h1>
<input type = "text" name="food">
%s
<button>Add</button>
</form>
"""

hidden_html="""
<input type="hidden" name="food" value=%s>
"""
item_html="<li>%s</li>"

Shopping_list_html="""
<br>
<br>
<h2>Shopping List </h2>
<ul>
%s
</ul>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        output=form_html
        hidden_output=""

        items=self.request.get_all("food")
        if items:
            output_items=""
            for item in items:
                hidden_output=hidden_output+hidden_html %item
                output_items=output_items+item_html %item
            output_Shopping=Shopping_list_html %output_items
            output = output+ output_Shopping
        output = output % hidden_output

        self.response.out.write(output)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from views.category_requests import create_category, get_all_categories
from views.postTag_requests import create_post_tag, get_all_post_tags
from views.post_requests import update_post
from views.tag_requests import get_single_tag
from views.user import create_user, login_user
from views import (get_all_posts, get_all_tags, get_single_post, create_post, create_tag, delete_post,
    get_all_post_tags, create_post_tag, update_tag, get_single_tag
)
from views.user_request import get_all_users, get_single_user


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self):
        """Parse the url into the resource and id"""
        path_params = self.path.split('/')
        resource = path_params[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        response = {}
        parsed = self.parse_url()
        if '?' in response:
            (resource, key, value) = parsed
        else:
            (resource, id) = parsed

        if resource == "posts":
            if id is not None:
                self._set_headers(200)
                response = get_single_post(id)
            else:
                self._set_headers(200)
                response = get_all_posts()

        elif resource == "tags":
            if id is not None:
                self._set_headers(200)
                response = get_single_tag(id)
            else:
                self._set_headers(200)
                response = get_all_tags()

        elif resource == "categories":
            self._set_headers(200)
            response = get_all_categories()
        elif resource == "postTags":
            self._set_headers(200)
            response = get_all_post_tags()
        elif resource == "users":
            if id is not None:
                self._set_headers(200)
                response = get_single_user(id)
            else:
                self._set_headers(200)
                response = get_all_users()
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url()

        if resource == 'login':
            response = login_user(post_body)
        elif resource == 'register':
            response = create_user(post_body)
        elif resource == 'postTags':
            response = create_post_tag(post_body)
        elif resource == 'tags':
            if 'label' in post_body:
                self._set_headers(201)
                response = create_tag(post_body)
        elif resource == 'categories':
            if 'label' in post_body:
                self._set_headers(201)
                response = create_category(post_body)
            else:
                self._set_headers(400)
                response = {"message": f'{"Label is required" if "label" not in post_body else""}'}
        if resource == 'posts':
            response = create_post(post_body)

        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url()

        success = False

        if resource == "posts":
            success = update_post(id, post_body)
            if success:
                self._set_headers(204)
            else:
                self._set_headers(404)

            self.wfile.write("".encode())

        if resource == "tags":
            success = update_tag(id, post_body)
            if success:
                self._set_headers(204)
            else:
                self._set_headers(404)

            self.wfile.write("".encode())

    def do_DELETE(self):
        """Handle DELETE Requests"""
        self._set_headers(204)
        (resource, id) = self.parse_url()
        response = None
        if resource == "posts":
            delete_post(id)
            self.wfile.write(json.dumps(response).encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()

Personal portfolio two
-------------

**1. admin.py**

Wrote logic for our admin page to restrict viewing of properties to only those they had the correct permissions for. Also wrote the logic to restrict read/write abilities to only staff/admin depending on their privileges (e.g. only admin can change the manager associated with a property.) Also wrote the logic to restrict deleting properties to only the admin.

**2. models.py**

Added owner and manager foreignkey fields, these utilise Django's User module from auth.models allowing us to create owner/manager accounts and assign them to properties at will from the admin page or python shell. These accounts in conjunction with the logic in admin.py allow us to create groups and a simple permission system to restrict CRUD operations to only users with sufficient privileges.

**3. tests.py**

Added code to instantiate dummy properties and user accounts for our selenium and django tests to use, these are contained in the create_user_test_accounts function (line 22). This allows us to automatically test user account permissions and the admin page.

**4. peer-review-two.pdf**

Wrote the entirety of the peer review and responded to/incorporated suggestions from other group members. Also engaged in communication with our client group (24) in order to share our suggestions and respond to theirs.

**5. base.html**

Provided initial custom templates for our admin page, and showed group the method for overwriting Django's default CSS and HTML for those pages. Also fixed a variety of small CSS/HTML bugs over the entire site.

# Overview

This is a sample Python web application using Flask that is protected via an Apereo CAS server using the [Flask CAS extension](https://github.com/cameronbwhite/Flask-CAS).

# Installation

- Python

```console
pip install -r requirements.txt
```

# Run

```console
$ python app.py

...

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 120-601-740
```

# Test

Navigate to `http://localhost:5000` and click on the login button.
You will be redirected to a CAS server to authenticate and once you return,
you should see the authenticated user id plus any and all attributes that
the server may have authorized you to receive.

![image](https://cloud.githubusercontent.com/assets/1205228/24905959/19cfc362-1ecb-11e7-8ac8-3dcdb82b9303.png)

Remember that the application must be registered with the CAS server, and 
should be authorized to authenticate.

You can find valid username and password under `cas.authn.accept.users` part of [CAS configuration part of CAS server dashboard](https://casserver.herokuapp.com/cas/status/config). It's `casuser`:`Mellon` for version 5.


# Configuration

CAS configuration may be specified in `app.py`:

```python
app.config['CAS_SERVER'] = 'https://jasigcas.herokuapp.com' 
app.config['CAS_AFTER_LOGIN'] = 'secure'
```

For all other relevant settings, please refer to the [Flask CAS extension](https://github.com/cameronbwhite/Flask-CAS) project.


OAuth:

customizable parameter in line 36 in templates/index.html:
- client_id
- redirect_uri

reference: https://apereo.github.io/cas/6.2.x/installation/OAuth-OpenId-Authentication.html#endpoints
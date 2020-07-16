# QuickVue

This is a seed project that I use to get sites up quickly using [Flask](http://flask.pocoo.org/) as a backend and [Vue](https://vuejs.org/).

Also includes other technologies I frequently use:
* [Flask Security](https://pythonhosted.org/Flask-Security/)
* [Peewee](http://docs.peewee-orm.com/en/latest/)
* [SQLite](https://www.sqlite.org/)
* [Marshmallow](https://marshmallow.readthedocs.io) for serialization
* [Semantic UI](https://semantic-ui.com/) for quick UI prototyping

Client scripts from [UNPKG](https://unpkg.com/) - no build systems here.

## Use

Requires Python 3: `bash start.sh`. The setup script is mostly for me to use with the Linux Subsystem for Windows. 

Default secrets are found in `config/secrets.yml`, actual secrets go in `config/secrets-override.yml` - which should not be checked into version control.

### Clone and rename workflow

To start a new project, named `awesome-project`:

```bash
git clone git@github.com:radusuciu/quickvue.git awesome-project
cd awesome-project
bash rename.sh awesome-project
rm -rf .git
rm rename.sh
git init
```

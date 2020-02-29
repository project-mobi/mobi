# Authentication <!-- omit in toc -->

## Contents <!-- omit in toc -->
- [Ory Oathkeeper](#ory-oathkeeper)
- [Ory Kratos](#ory-kratos)
  - [Configuration](#configuration)
  - [Registration / Onboarding](#registration--onboarding)
  - [User roles](#user-roles)
    - [default roles](#default-roles)
  - [Users json schema](#users-json-schema)
- [Frontend](#frontend)




## Ory Oathkeeper
proxy to protect apis, works with nginx auth_request

## Ory Kratos
API only user and identity management
[Quickstart guide](https://www.ory.sh/docs/kratos/quickstart). Build from there

### Configuration
If file $HOME/.kratos.yaml exists, it will be used as a configuration file which supports all configuration settings listed below.
Config files can be formatted as JSON, YAML and TOML. Some configuration values support reloading without server restart. All configuration values can be set using environment variables, as documented below. This allows us to extrapolate all configuration to the docker-compose file. For a complete reference of all configuration options visit the Kratos [docs](https://www.ory.sh/docs/kratos/reference/configuration) page.

### Registration / Onboarding
There should be three differnet onboarding flows.
1. SysAdmin / HR Role creates users
2. Users with an invite link can self register
3. Completely open registration to anyone
   


### User roles
Nested structure. Kratos has main roles. Service roles synced with kratos. 

#### default roles
- Manager
  - OpenProject
    - Create project
  - Mattermost
    - Create channel
    - Add people to channel
- Employee
  - OpenProject
    - Add task to project
  - Mattermost
    - Send message
- Admin
  - Everything, everywhere
- Guest/Freelancer
  - Temporary
  - Only for specific 

### Users json schema
Kratos uses json schemas to differentiate between types of users. There are default fields that apply to everyone and for each role we extend this schema.

```json
{
    "$id": "http://example.com/product.schema.json",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "User",
    "description": "A User int the mobi cloud",
    "type": "object",
    "properties": {
        "userId": {
        "description": "The unique identifier for a user",
        "type": "integer"
        },
        "name": {
            "type": "object",
            "properties": {
                "first": {
                    "description": "The user's first name",
                    "type": "string"
                },
                "last" : {
                    "description": "The user's last name",
                    "type": "string"
                }
            }
        },
        "email": {
            "description": "email address for the user",
            "type": "string",
            "format": "email",
            "ory.sh/kratos": {
                "credentials": {
                    "password": {
                        "identifier": true
                    }
                }
            }
        },
        "phoneNumber": {
            "description": "user's phone number",
            "type": "string",
        }
    },
    "required": [ "userId" ]
    additionalProperties: false,
}
```
## Frontend
Kratos has no build in frontend UI. This is something we will have to implement.
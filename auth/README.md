# Authentication <!-- omit in toc -->

## Contents <!-- omit in toc -->
- [Ory backend](#ory-backend)
  - [Oathkeeper](#oathkeeper)
  - [Kratos](#kratos)
    - [User roles](#user-roles)
- [Frontend](#frontend)


## Ory backend

### Oathkeeper
proxy to protect apis, works with nginx auth_request

### Kratos
User and identity management
[Quickstart guide](https://www.ory.sh/docs/kratos/quickstart). Build from there

#### User roles
Nested structure. Kratos has main roles. Service roles synced with kratos

**roles**
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

## Frontend
Kratos has no build in frontend UI. This is something we will have to implement.
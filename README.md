# Yume auth

<div align="center">
  <img align="center"  width="auto" height="auto" src="/assets/logo.png" />
  <br/>

  <div id="user-content-toc">
    <ul>
      <summary>
      <h1 style="display: inline-block;">Yume</h1>
      <br/>
      <h3 style="display: inline-block;">The AI-powered social wish-list platform</h3>
      </summary>
    </ul>
  </div>
</div>

Yume auth is the micro-service that handles the authorization, authentication and security-based requests of [Yume](https://yume.so).

This is a micro-service to serve as an example of how to develop an scalable (architecture & tech) micro-service using python, flask and a combination oh _HTTP_ & _Event-based_ requets

- [Yume auth](#yume-auth)
  - [Gettings started](#gettings-started)
  - [Local development (**In progress**)](#local-development-in-progress)
  - [Project structure](#project-structure)
  - [Development convections](#development-convections)
    - [Branch naming](#branch-naming)
    - [Branch reference](#branch-reference)
    - [Branch description](#branch-description)
    - [Branch name examples](#branch-name-examples)
    - [Convectional commits](#convectional-commits)
  - [Testing](#testing)
  - [Yume related repositories](#yume-related-repositories)
  - [References](#references)
  - [License](#license)

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

## Gettings started

Clone the repository

```sh
git clone https://gagocarrilloedgar/yume-auth
```

## Local development (**In progress**)

Install the dependencies, take a look at [Python with pipenv](https://realpython.com/pipenv-guide/) for more info.

```sh
pipenv shell
pipenv install
```

Run the migrations

```sh
pipenv run migrate
pipenv run upgrade
```

And start the server:

```sh
# Copy the env.example file
cp .env.example .env

#Start it
pipenv start
```

Formating and linting

- https://www.jumpingrivers.com/blog/python-linting-guide/
- pylint
- https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/

## Project structure

[TBD]

## Development convections

This section provide the branc, commit adn test convection for working with the project while following best practices

### Branch naming

A git branch should start with a category. Pick one of these: _feature_, _bugfix_, _hotfix_, or _test_:

- **feature** is for adding, refactoring or removing a feature.
- **bugfix** is for fixing a bug.
- **hotfix** is for changing code with a temporary solution and/or without following the usual process (usually because of an emergency).
- **test** is for experimenting outside of an issue/ticket.

### Branch reference

After the category, there should be a `/` followed by the reference of the _issue/ticket_ you are working on. If there's no reference, just add `no-ref`.

### Branch description

After the reference, there should be another `/` followed by a description which sums up the purpose of this specific branch. This description should be short and `"kebab-cased"`.

By default, you can use the title of the issue/ticket you are working on. Just replace any special character by "-".

### Branch name examples

```sh
git branch <category/reference/description-in-kebab-case>
```

- You need to add, refactor or remove a feature: `git branch feature/<notion-story-id>/create-new-button-component`
- You need to fix a bug: git branch `bugfix/<notion-story-id>/button-overlap-form-on-mobile`
- You need to fix a bug really fast (possibly with a temporary solution): `git branch hotfix/no-ref/registration-form-not-working`
- You need to experiment outside of an issue/ticket: `git branch test/no-ref/refactor-components-with-atomic-design`

### Convectional commits

The Conventional Commits specification is a lightweight convention on top of commit messages. If you want to read more about it: [Conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)

[TBD]-> Look for husky and lint-staged alternatives in Python:

- https://pre-commit.com/
- https://pypi.org/project/autohooks/

The tipical categories are:

- _feat_ is for adding a new feature
- _fix_ is for fixing a bug
- _refactor_ is for changing code for peformance or convenience purpose (e.g. readibility)
- _chore_ is for everything else (writing documentation, formatting, adding tests, cleaning useless code etc.)
- _docs_ is to add documentation (readme, swagger, storybook, etc).

If you event wan to add more semantic to the commit you add a scope:

```sh
git commit <category(scope): description>
```

One example could be (taking into account you are developing something related to the layout and its a new feature).

```sh
git commit <feat(layout): sidenav redirection added>
```

## Testing

[TBD]

## Yume related repositories

For more info regarding all the repositories that include Yume take a look at: [Yume's github](https://github.com/yumedotso)

## References

- https://github.com/serfer2/flask-hexagonal-architecture-api
- https://github.com/Shihara-Dilshan/John-Keells-App-Revamp
- https://auth0.com/blog/best-practices-for-flask-api-development/
- https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/
- https://github.com/bajcmartinez/flask-api-starter-kit

## License

[MIT](/LICENSE)

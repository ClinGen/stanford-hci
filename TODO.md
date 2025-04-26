# Things That Need to Be Done Before User Testing on May 5th

## We're done refactoring. 

- [x] Templates have been refactored to match routes as much as possible.
    - See [the routes test](./src/tests/integration/routes_test.py).
    - For example, `markers/new_allele.html` should be `markers/allele/new.html`.
    - [x] We've found all templates where this refactor is needed.
    - [x] We've made the changes.

- [x] Create an integration test that makes sure all routes return a 200 status code.

- [x] We no longer prepend includes with underscores.
- [ ] Includes have been refactored to be inside their app namespace.
    - [ ] We've found all templates where this refactor is needed.
    - [ ] We've made the changes.
        - [ ] curations
        - [ ] diseases
        - [ ] home
        - [ ] markers
        - [ ] publications
        - [ ] users

- [ ] Views have been refactored.
    - For example, `views/new_allele.py` should be `views/allele.py`.
    - [ ] We've found all views where this refactor is needed.
    - [ ] We've made the changes.

- [ ] Abstract base classes are in use.
    - [ ] Clients implement an abstract base class.
    - [ ] Selectors implement an abstract base class.
    - [ ] Services implement an abstract base class.
    - [ ] Views implement an abstract base class.

## The missing tests have been added.

- [ ] We've found all modules that are missing tests.
- [ ] We've added the tests.

## The `reorg` branch is merged into the `main` branch.

- [x] We've extracted all tasks from my personal to-do list.

- [x] The documentation system is set up.
    - [x] We have a document for how-to guides.
    - [x] We have a document for tutorials.
    - [x] We have a document for explanations.
    - [x] The README links to the documentation.

- [ ] We've fixed the type check issues.
- [ ] All TODOs in the code have been resolved.
- [ ] We are linting Django templates as part of code quality checks.
- [ ] The score calculator code is integrated.
- [ ] All code quality checks are passing.
- [ ] We are using conventional commits.
- [ ] The garbage development migrations are blown away.
- [ ] The commit history is restricted to the new organization of the code and the new commit convention.
    - (The prior history is too messy to be useful.)

## MVP functionality is complete.

- [ ] Models have a human-readable ID.
    - Ideas:
        - `AL`: denotes allele
        - `HP`: denotes haplotype
        - `ALC`: denotes allele curation
        - `HPC`: denotes haplotype curation
        - `ALA`: denotes allele association
        - `HPA`: denotes haplotype association

- [ ] The basic workflow for the app is in place.
    - [x] The user can sign up.
    - [ ] The user can log in.
    - [ ] The user can log out.
        - [ ] When the user signs up, their curator object is created.
    - [ ] The user can view their curations on the home page.
    - [ ] The user can add a curation.
    - [x] The user can add a disease.
    - [x] The user can add a marker.
    - [x] The user can add a publication.
    - [ ] The user can view all curations.
    - [ ] The user can view all diseases.
    - [ ] The user can view all markers.
    - [x] The user can view all publications.
    - [ ] The user can curate.

- [ ] We have end-to-end tests for all workflows.
    - [ ] sign up
    - [ ] log in
    - [ ] log out
    - [ ] view all curations on the home page when logged out
    - [ ] view your curations on the home page when logged in
    - [ ] click all buttons on the home page
    - [ ] add a curation
    - [ ] add a disease
    - [ ] add a marker
    - [ ] add a publication
    - [ ] view all curations
    - [ ] view all diseases
    - [ ] view all markers
    - [ ] view all publications
    - [ ] curate

- [ ] The data validation plan has been implemented.
    - The three different validation layers:
        - 1: Basic checking that we actually got what we needed in the client
        - 2: Decoupled "validators" (possibly Pydantic) that make sure the data conforms to what we expect
        - 3: Django validators in the models to perform extra checks

## All miscellaneous tasks have been resolved.

- [ ] In the UI, the underscore in the Mondo ID should be a colon.
    - [ ] The code transforms the underscore into a colon.
- [ ] There is an include for help text
    - [ ] All help texts use this include.

## The app test deployed to the test server and the prod server.

- [ ] The test server is running the HCI with all MVP functionality.
- [ ] The prod server is running the HCI with all MVP functionality.

## Nice-to-have tasks are complete.

- [ ] We have the following CI workflow: PR opened → checks pass → deploy to test.
- [ ] We have the following CI workflow: PR approved and merged → deploy to prod.
- [ ] We have a footer in Ingrid's purple.
- [ ] The help text can be edited by non-developers.
- [ ] We have a Sphinx dev docs site.
- [ ] We have the following CI workflow: PR opened → check dev docs site.
- [ ] We have the following CI workflow: PR approved and merged → deploy dev docs.
- [ ] We've added Firebase.

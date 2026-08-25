# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>


## Implementation


### Phase 1

- Forked the main directory and created branches of the forked directory.
- Created a project board using Kanban template.
- Delivered the initial phase as a pull request, which I will do for each next phase.

###  Phase 2
- Implemented a python app which runs a basic print version function.
- Tested it locally with a Docker container.
- To test the app: docker run hivebox:0.0.1
- Output: HiveBox Vesrion: 0.0.1

###  Phase 3
- Implemented Flask API with `/version` and `/temperature` endpoints.
- `/temperature` fetches data from openSenseMap API and returns average temperature (data max 1 hour old).
- Added unit tests for both endpoints using pytest.
- Added Dockerfile with best practices.
- Added GitHub Actions CI pipeline: lint Dockerfile, lint Python, run unit tests, build image, test `/version` endpoint.
- Added OpenSSF Scorecard for security scanning.

###  Phase 4
- Added Kubernetes manifests: Deployment, Service, Ingress, ConfigMap
- Kind cluster config with Ingress-Nginx
- `/metrics` endpoint with Prometheus metrics
- `status` field on `/temperature` response
- SenseBox IDs are now configurable via env vars
- Integration tests with VCR.py
- Implemented SonarQube and Terrascan in CI pipeline
- CD workflow to push images to GHCR
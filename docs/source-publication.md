# Publishing public source

The [Publish Public Source workflow](../.github/workflows/publish-source.yaml)
is a thin manual caller of the central
[`niaid/nephele_gh_actions` action](https://github.com/niaid/nephele_gh_actions/tree/main/.github/actions/publish-source).
All validation, authentication, export, synchronization, and integration-test
logic lives in that central repository.

The destination is `niaid/nephele_wgsa2_pub`, derived using
`OWNER/SOURCE_REPOSITORY_NAME_pub`. This repository owns the explicit
[publication allowlist](../.github/source-export.txt), including the root README
and license, pipeline code, configuration, templates, and required lookup tables.
New files are not published automatically. Remove an allowlist entry when
removing a published file.

## Setup and operation

Follow the central action's setup instructions:

1. Publish the shared action to the central repository's `main` branch first.
   If it is private, enable Actions access for this repository.
2. Review every allowlisted file for credentials, internal-only information,
   and redistribution permissions before making it public.
3. Create the empty public destination repository.
4. Install a GitHub App on only that destination, granting Contents read/write.
5. In this repository, create the `public-source` Actions environment with
   required reviewers and default-branch deployment restrictions. Set environment
   variable `SOURCE_EXPORT_APP_ID` and secret `SOURCE_EXPORT_APP_PRIVATE_KEY`.
6. Ensure Actions policies permit the shared action and its dependencies, and
   the destination branch rules permit the App to push.
7. Run **Actions > Publish Public Source > Run workflow** on the default branch
   and approve the protected environment deployment.

Only committed, allowlisted files are exported. Source Git history, PDFs,
infrastructure, and workflows are not copied. The public repository has its own
snapshot history; unchanged runs make no commit, and pushes are never forced.
The entire destination `nephele_wgsa2/` directory and root `README.md` and `LICENSE`
are managed by the action, including deletions. Other root paths are preserved.

This is not a standalone runtime bundle. `config.json` still references an
excluded output-details PDF, and dependencies such as `nephele_pipeline_utils`
are not bundled. Existing pipeline behavior is unchanged.

## Validation

The integration tests and export helper now live in `nephele_gh_actions`.
See the central action's documentation for local validation commands. The
shared action runs its integration tests before authenticating to the public
destination. No helper scripts need to be maintained in this repository.

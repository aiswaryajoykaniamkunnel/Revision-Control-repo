const { GitHub } = require('@actions/github');
const github = new GitHub(process.env.GITHUB_TOKEN);

const secretValue = 'new_secret_value';
const owner = process.env.GITHUB_REPOSITORY.split('/')[0];
const repo = process.env.GITHUB_REPOSITORY.split('/')[1];
const secretName = 'REPO_VARIABLE'; // Replace with your secret name

async function updateSecret() {
    try {
        const response = await github.actions.createOrUpdateRepoSecret({
            owner,
            repo,
            secret_name: secretName,
            encrypted_value: Buffer.from(secretValue).toString('base64')
        });
        console.log('Secret updated successfully:', response.data);
    } catch (error) {
        console.error('Error updating secret:', error);
        process.exit(1);
    }
}

updateSecret();
module.exports = {
    env: {
        browser: true,
        node: true,
        es2021: true
    },
    extends: [
        'eslint:recommended'
    ],
    parserOptions: {
        ecmaVersion: 12,
        sourceType: 'module'
    },
    rules: {
        // enforce semicolons
        'semi': ['error', 'always'],
        // enforce camelCase naming
        'camelcase': ['error', { properties: 'never' }],
        // enforce single quotes
        'quotes': ['error', 'single']
    }
};
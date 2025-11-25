# Example Composite Action

This is an example of a Composite Action. It demonstrates how to use a Composite Action in GitHub Actions to run a series of steps with inputs and outputs.

## Inputs

- `MANDATORY_INPUT`: A mandatory input for the action.
- `OPTIONAL_INPUT_1`: An optional input with a default value.
- `OPTIONAL_INPUT_2`: An optional input that can be set to true or false.
- `OPTIONAL_INPUT_3`: Another optional input that can be set to true or false

## Usage

You can use this action in your workflow like this:

```yaml
uses: ./actions/demo_action
with:
  MANDATORY_INPUT: "value1"
  OPTIONAL_INPUT_1: "value2"
  OPTIONAL_INPUT_2: "true"
  OPTIONAL_INPUT_3: "false"
```

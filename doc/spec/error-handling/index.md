# Error Handling

This section documents error definitions. Errors define failure outcomes
for Functional Requirements - what happens when an operation fails.

## Error Definition Structure

Each error SHALL include:

*   **Description**: Semantic meaning of the error
*   **Triggers**: Conditions that cause the error
*   **Outcome**: Observable result when the error occurs
*   **Related Requirements**: FRs that may produce this error
*   **Constraints**: CONs that restrict error handling (if applicable)

- [auth](auth.md)
- [validation](validation.md)
- [resource](resource.md)
- [rate-limit](rate-limit.md)
- [system](system.md)
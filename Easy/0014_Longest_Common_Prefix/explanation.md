
### `explanation.md`

```markdown
# Explanation - Longest Common Prefix

The goal is to find the longest sequence of characters that appears at the beginning of every string.

For example:

["flower", "flow", "flight"]

Start with:

prefix = "flower"

Compare with "flow":

"flow" does not start with "flower"

Remove characters from the end:

"flower" -> "flowe" -> "flow"

Now compare "flow" with "flight":

"flight" does not start with "flow"

Shorten the prefix:

"flow" -> "flo" -> "fl"

Now:

"flight".startswith("fl")

returns True.

Therefore, the longest common prefix is:

"fl"

## Python Concept Used

### startswith()

`startswith()` checks whether a string begins with another string.

Example:

"flight".startswith("fl")

returns:

True

### String slicing

`prefix[:-1]` removes the last character.

Example:

"flower"[:-1]

returns:

"flowe"

## Complexity

Time Complexity: O(S)

Space Complexity: O(1)
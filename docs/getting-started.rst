Getting started
===============

For backward compatibility in previous version only `--[yaml|json|toml|ini|xml|hcl]` was possible with default to json output.
We still keep Monochrome, raw and json output with thoses options.
Output was similar to `jq -MCr` (no color, no compact and no quote on single value)

But now, by default it's colorized, not raw and if you specify input using `-i` or `--input` output will be the same format.

There is also a shorter command `wq` comming with the package.

Like `jq cli`, wildq supports both of stdin and file to the function

See examples to get some example.

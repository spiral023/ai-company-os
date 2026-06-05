param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Args
)

python "$PSScriptRoot\ai.py" @Args

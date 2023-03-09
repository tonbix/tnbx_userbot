# Add new commands guide

1. Create `{{commandFileName}}.py` file in `./handlers` and put this inside:

    ```python
    class {{CommandName}}:
        # command settings
        def __init__(self) -> None:
            self.enabled: bool  # enable/disable command
            self.aliases: tuple # aliases for command
            self.usage: str     # string with usage. Example: "-/{{passes amount}}"
            self.description: str   # description of command


        async def function(self) -> None:
            # here's your command
    ```

2. In `handlers/__init__.py` add this line

    ```python
    from .{{commandFileName}} import {{CommandName}}
    ```

3. Inside `commandsHandler.py` in `commandsList` on line 43 append

    ```python
    [{{CommandName}}(), [*args]]
    ```

4. And inside `handlers/help.py` in `commands` on line 31 append

    ```python
    {{CommandName}}()
    ```

After all you can restart bot and call your command by one of aliases. Also it will appear in help command

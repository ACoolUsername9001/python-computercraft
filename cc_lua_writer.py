from io import FileIO


class LuaWriter(FileIO):

    def write(self, __s: str, write: bool = True) -> str:
        if write:
            super(LuaWriter, self).write(bytes(__s, 'utf-8'))

        return __s[0:-1] if __s[-1] == '\n' else __s

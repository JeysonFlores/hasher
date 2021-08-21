import subprocess

schemadir = "/usr/local/share/glib-2.0/schemas"

try:
    print("- Compiling GSchemas...")
    subprocess.call(['glib-compile-schemas', schemadir])
    print("- GSchemas compiled")
except Exception as e:
    print("- GSchemas compilation failed...")
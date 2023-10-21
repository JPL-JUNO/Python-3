"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-21 11:45:08
@Description: 
"""
import configparser

option_name = [
    'from-default',
    'from-section', 'section-only',
    'file-only', 'init-only', 'init-and-file',
    'from-vars',
]

# 初始化一个 parser 的默认值
# 表示为默认配置
DEFAULTS = {
    'from-default': 'value from defaults passed to init',
    'init-only': 'value from defaults passed to init',
    'init-and-file': 'value from defaults passed to init',
    'from-section': 'value from defaults passed to init',
    'from-vars': 'value from defaults passed to init',
}

parser = configparser.ConfigParser(defaults=DEFAULTS)


print('Defaults before loading file:')
defaults = parser.defaults()

for name in option_name:
    if name in defaults:
        print('  {:<15} = {!r}'.format(name, defaults[name]))

parser.read('with-default.ini')

# 覆盖一些默认配置
print('\nDefaults after loading file:')
defaults = parser.defaults()
for name in option_name:
    if name in defaults:
        print(' {:<15} = {!r}'.format(name, defaults[name]))


vars = {'from-vars': 'value from vars'}
# var 这个字典的优先级更高，甚至可以覆盖一些配置文件中的配置选项
print('\nOption lookup:')
for name in option_name:
    value = parser.get('sect', name, vars=vars)
    print('  {:<15} = {!r}'.format(name, value))

print('\nError cases:')
try:
    print('No such option :', parser.get('sect', 'no-option'))
except configparser.NoOptionError as err:
    print(err)

try:
    print('No such section:', parser.get('no-sect', 'no-option'))
except configparser.NoSectionError as err:
    print(err)

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


# Originally based on FlaskyStyle which was based on 'tango'.
class Alabaster(Style):
    background_color = "#f8f8f8" # doesn't seem to override CSS 'pre' styling?
    default_style = ""

    styles = {
        # No corresponding class for the following:
        #Text:                     "", # class:  ''
        Whitespace:                "underline #f8f8f8",      # class: 'w'
        Error:                     "#a40000 border:#ef2929", # class: 'err'
        Other:                     "#000000",                # class 'x'

        Comment:                   "italic #8f5902", # class: 'c'
        Comment.Preproc:           "noitalic",       # class: 'cp'

        Keyword:                   "bold #004461",   # class: 'k'
        Keyword.Constant:          "bold #004461",   # class: 'kc'
        Keyword.Declaration:       "bold #004461",   # class: 'kd'
        Keyword.Namespace:         "bold #004461",   # class: 'kn'
        Keyword.Pseudo:            "bold #004461",   # class: 'kp'
        Keyword.Reserved:          "bold #004461",   # class: 'kr'
        Keyword.Type:              "bold #004461",   # class: 'kt'

        Operator:                  "#582800",   # class: 'o'
        Operator.Word:             "bold #004461",   # class: 'ow' - like keywords

        Punctuation:               "bold #000000",   # class: 'p'

        # because special names such as Name.Class, Name.Function, etc.
        # are not recognized as such later in the parsing, we choose them
        # to look the same as ordinary variables.
        Name:                      "#000000",        # class: 'n'
        Name.Attribute:            "#c4a000",        # class: 'na' - to be revised
        Name.Builtin:              "#004461",        # class: 'nb'
        Name.Builtin.Pseudo:       "#3465a4",        # class: 'bp'
        Name.Class:                "#000000",        # class: 'nc' - to be revised
        Name.Constant:             "#000000",        # class: 'no' - to be revised
        Name.Decorator:            "#888",           # class: 'nd' - to be revised
        Name.Entity:               "#ce5c00",        # class: 'ni'
        Name.Exception:            "bold #cc0000",   # class: 'ne'
        Name.Function:             "#000000",        # class: 'nf'
        Name.Property:             "#000000",        # class: 'py'
        Name.Label:                "#f57900",        # class: 'nl'
        Name.Namespace:            "#000000",        # class: 'nn' - to be revised
        Name.Other:                "#000000",        # class: 'nx'
        Name.Tag:                  "bold #004461",   # class: 'nt' - like a keyword
        Name.Variable:             "#000000",        # class: 'nv' - to be revised
        Name.Variable.Class:       "#000000",        # class: 'vc' - to be revised
        Name.Variable.Global:      "#000000",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "#000000",        # class: 'vi' - to be revised

        Number:                    "#990000",        # class: 'm'

        Literal:                   "#000000",        # class: 'l'
        Literal.Date:              "#000000",        # class: 'ld'

        String:                    "#4e9a06",        # class: 's'
        String.Backtick:           "#4e9a06",        # class: 'sb'
        String.Char:               "#4e9a06",        # class: 'sc'
        String.Doc:                "italic #8f5902", # class: 'sd' - like a comment
        String.Double:             "#4e9a06",        # class: 's2'
        String.Escape:             "#4e9a06",        # class: 'se'
        String.Heredoc:            "#4e9a06",        # class: 'sh'
        String.Interpol:           "#4e9a06",        # class: 'si'
        String.Other:              "#4e9a06",        # class: 'sx'
        String.Regex:              "#4e9a06",        # class: 'sr'
        String.Single:             "#4e9a06",        # class: 's1'
        String.Symbol:             "#4e9a06",        # class: 'ss'

        Generic:                   "#000000",        # class: 'g'
        Generic.Deleted:           "#a40000",        # class: 'gd'
        Generic.Emph:              "italic #000000", # class: 'ge'
        Generic.Error:             "#ef2929",        # class: 'gr'
        Generic.Heading:           "bold #000080",   # class: 'gh'
        Generic.Inserted:          "#00A000",        # class: 'gi'
        Generic.Output:            "#888",           # class: 'go'
        Generic.Prompt:            "#745334",        # class: 'gp'
        Generic.Strong:            "bold #000000",   # class: 'gs'
        Generic.Subheading:        "bold #800080",   # class: 'gu'
        Generic.Traceback:         "bold #a40000",   # class: 'gt'
    }


class LightStyle(Style):
    """
    The Solarized Light style, inspired by Schoonover.
    """
    background_color = '#fdf6e3'
    default_style = ""

    styles = {
        Text:                   '#657b83',             # base00 ; class: ''
        Whitespace:             '#fdf6e3',             # base3  ; class: 'w'
        Error:                  '#dc322f',             # red    ; class: 'err'
        Other:                  '#657b83',             # base00 ; class: 'x'

        Comment:                'italic #93a1a1',      # base1  ; class: 'c'
        Comment.Multiline:      'italic #93a1a1',      # base1  ; class: 'cm'
        Comment.Preproc:        'italic #93a1a1',      # base1  ; class: 'cp'
        Comment.Single:         'italic #93a1a1',      # base1  ; class: 'c1'
        Comment.Special:        'italic #93a1a1',      # base1  ; class: 'cs'

        Keyword:                '#859900',             # green  ; class: 'k'
        Keyword.Constant:       '#859900',             # green  ; class: 'kc'
        Keyword.Declaration:    '#859900',             # green  ; class: 'kd'
        Keyword.Namespace:      '#cb4b16',             # orange ; class: 'kn'
        Keyword.Pseudo:         '#cb4b16',             # orange ; class: 'kp'
        Keyword.Reserved:       '#859900',             # green  ; class: 'kr'
        Keyword.Type:           '#859900',             # green  ; class: 'kt'

        Operator:               '#657b83',             # base00 ; class: 'o'
        Operator.Word:          '#859900',             # green  ; class: 'ow'

        Name:                   '#586e75',             # base01 ; class: 'n'
        Name.Attribute:         '#657b83',             # base00 ; class: 'na'
        Name.Builtin:           '#268bd2',             # blue   ; class: 'nb'
        Name.Builtin.Pseudo:    'bold #268bd2',        # blue   ; class: 'bp'
        Name.Class:             '#268bd2',             # blue   ; class: 'nc'
        Name.Constant:          '#b58900',             # yellow ; class: 'no'
        Name.Decorator:         '#cb4b16',             # orange ; class: 'nd'
        Name.Entity:            '#cb4b16',             # orange ; class: 'ni'
        Name.Exception:         '#cb4b16',             # orange ; class: 'ne'
        Name.Function:          '#268bd2',             # blue   ; class: 'nf'
        Name.Property:          '#268bd2',             # blue   ; class: 'py'
        Name.Label:             '#657b83',             # base00 ; class: 'nc'
        Name.Namespace:         '#b58900',             # yellow ; class: 'nn'
        Name.Other:             '#657b83',             # base00 ; class: 'nx'
        Name.Tag:               '#859900',             # green  ; class: 'nt'
        Name.Variable:          '#cb4b16',             # orange ; class: 'nv'
        Name.Variable.Class:    '#268bd2',             # blue   ; class: 'vc'
        Name.Variable.Global:   '#268bd2',             # blue   ; class: 'vg'
        Name.Variable.Instance: '#268bd2',             # blue   ; class: 'vi'

        Number:                 '#2aa198',             # cyan   ; class: 'm'
        Number.Float:           '#2aa198',             # cyan   ; class: 'mf'
        Number.Hex:             '#2aa198',             # cyan   ; class: 'mh'
        Number.Integer:         '#2aa198',             # cyan   ; class: 'mi'
        Number.Integer.Long:    '#2aa198',             # cyan   ; class: 'il'
        Number.Oct:             '#2aa198',             # cyan   ; class: 'mo'

        Literal:                '#657b83',             # base00 ; class: 'l'
        Literal.Date:           '#657b83',             # base00 ; class: 'ld'

        Punctuation:            '#657b83',             # base00 ; class: 'p'

        String:                 '#2aa198',             # cyan   ; class: 's'
        String.Backtick:        '#2aa198',             # cyan   ; class: 'sb'
        String.Char:            '#2aa198',             # cyan   ; class: 'sc'
        String.Doc:             '#2aa198',             # cyan   ; class: 'sd'
        String.Double:          '#2aa198',             # cyan   ; class: 's2'
        String.Escape:          '#cb4b16',             # orange ; class: 'se'
        String.Heredoc:         '#2aa198',             # cyan   ; class: 'sh'
        String.Interpol:        '#cb4b16',             # orange ; class: 'si'
        String.Other:           '#2aa198',             # cyan   ; class: 'sx'
        String.Regex:           '#2aa198',             # cyan   ; class: 'sr'
        String.Single:          '#2aa198',             # cyan   ; class: 's1'
        String.Symbol:          '#2aa198',             # cyan   ; class: 'ss'

        Generic:                '#657b83',             # base00 ; class: 'g'
        Generic.Deleted:        '#657b83',             # base00 ; class: 'gd'
        Generic.Emph:           '#657b83',             # base00 ; class: 'ge'
        Generic.Error:          '#657b83',             # base00 ; class: 'gr'
        Generic.Heading:        '#657b83',             # base00 ; class: 'gh'
        Generic.Inserted:       '#657b83',             # base00 ; class: 'gi'
        Generic.Output:         '#657b83',             # base00 ; class: 'go'
        Generic.Prompt:         '#657b83',             # base00 ; class: 'gp'
        Generic.Strong:         '#657b83',             # base00 ; class: 'gs'
        Generic.Subheading:     '#657b83',             # base00 ; class: 'gu'
        Generic.Traceback:      '#657b83',             # base00 ; class: 'gt'
    }


class DarkStyle(Style):
    """
    The Solarized Dark style, inspired by Schoonover.
    """
    background_color = '#002b36'
    default_style = ""

    styles = {
        Text:                   '#839496',             # base0  ; class: ''
        Whitespace:             '#002b36',             # base03 ; class: 'w'
        Error:                  '#dc322f',             # red    ; class: 'err'
        Other:                  '#839496',             # base0  ; class: 'x'

        Comment:                'italic #586e75',      # base01 ; class: 'c'
        Comment.Multiline:      'italic #586e75',      # base01 ; class: 'cm'
        Comment.Preproc:        'italic #586e75',      # base01 ; class: 'cp'
        Comment.Single:         'italic #586e75',      # base01 ; class: 'c1'
        Comment.Special:        'italic #586e75',      # base01 ; class: 'cs'

        Keyword:                '#859900',             # green  ; class: 'k'
        Keyword.Constant:       '#859900',             # green  ; class: 'kc'
        Keyword.Declaration:    '#859900',             # green  ; class: 'kd'
        Keyword.Namespace:      '#cb4b16',             # orange ; class: 'kn'
        Keyword.Pseudo:         '#cb4b16',             # orange ; class: 'kp'
        Keyword.Reserved:       '#859900',             # green  ; class: 'kr'
        Keyword.Type:           '#859900',             # green  ; class: 'kt'

        Operator:               '#839496',             # base0  ; class: 'o'
        Operator.Word:          '#859900',             # green  ; class: 'ow'

        Name:                   '#93a1a1',             # base1  ; class: 'n'
        Name.Attribute:         '#839496',             # base0  ; class: 'na'
        Name.Builtin:           '#268bd2',             # blue   ; class: 'nb'
        Name.Builtin.Pseudo:    'bold #268bd2',        # blue   ; class: 'bp'
        Name.Class:             '#268bd2',             # blue   ; class: 'nc'
        Name.Constant:          '#b58900',             # yellow ; class: 'no'
        Name.Decorator:         '#cb4b16',             # orange ; class: 'nd'
        Name.Entity:            '#cb4b16',             # orange ; class: 'ni'
        Name.Exception:         '#cb4b16',             # orange ; class: 'ne'
        Name.Function:          '#268bd2',             # blue   ; class: 'nf'
        Name.Property:          '#268bd2',             # blue   ; class: 'py'
        Name.Label:             '#839496',             # base0  ; class: 'nc'
        Name.Namespace:         '#b58900',             # yellow ; class: 'nn'
        Name.Other:             '#839496',             # base0  ; class: 'nx'
        Name.Tag:               '#859900',             # green  ; class: 'nt'
        Name.Variable:          '#cb4b16',             # orange ; class: 'nv'
        Name.Variable.Class:    '#268bd2',             # blue   ; class: 'vc'
        Name.Variable.Global:   '#268bd2',             # blue   ; class: 'vg'
        Name.Variable.Instance: '#268bd2',             # blue   ; class: 'vi'

        Number:                 '#2aa198',             # cyan   ; class: 'm'
        Number.Float:           '#2aa198',             # cyan   ; class: 'mf'
        Number.Hex:             '#2aa198',             # cyan   ; class: 'mh'
        Number.Integer:         '#2aa198',             # cyan   ; class: 'mi'
        Number.Integer.Long:    '#2aa198',             # cyan   ; class: 'il'
        Number.Oct:             '#2aa198',             # cyan   ; class: 'mo'

        Literal:                '#839496',             # base0  ; class: 'l'
        Literal.Date:           '#839496',             # base0  ; class: 'ld'

        Punctuation:            '#839496',             # base0  ; class: 'p'

        String:                 '#2aa198',             # cyan   ; class: 's'
        String.Backtick:        '#2aa198',             # cyan   ; class: 'sb'
        String.Char:            '#2aa198',             # cyan   ; class: 'sc'
        String.Doc:             '#2aa198',             # cyan   ; class: 'sd'
        String.Double:          '#2aa198',             # cyan   ; class: 's2'
        String.Escape:          '#cb4b16',             # orange ; class: 'se'
        String.Heredoc:         '#2aa198',             # cyan   ; class: 'sh'
        String.Interpol:        '#cb4b16',             # orange ; class: 'si'
        String.Other:           '#2aa198',             # cyan   ; class: 'sx'
        String.Regex:           '#2aa198',             # cyan   ; class: 'sr'
        String.Single:          '#2aa198',             # cyan   ; class: 's1'
        String.Symbol:          '#2aa198',             # cyan   ; class: 'ss'

        Generic:                '#839496',             # base0  ; class: 'g'
        Generic.Deleted:        '#839496',             # base0  ; class: 'gd'
        Generic.Emph:           '#839496',             # base0  ; class: 'ge'
        Generic.Error:          '#839496',             # base0  ; class: 'gr'
        Generic.Heading:        '#839496',             # base0  ; class: 'gh'
        Generic.Inserted:       '#839496',             # base0  ; class: 'gi'
        Generic.Output:         '#839496',             # base0  ; class: 'go'
        Generic.Prompt:         '#839496',             # base0  ; class: 'gp'
        Generic.Strong:         '#839496',             # base0  ; class: 'gs'
        Generic.Subheading:     '#839496',             # base0  ; class: 'gu'
        Generic.Traceback:      '#839496',             # base0  ; class: 'gt'
    }
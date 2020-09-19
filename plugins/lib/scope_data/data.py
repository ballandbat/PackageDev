# https://www.sublimetext.com/docs/3/scope_naming.html
# https://manual.macromates.com/en/language_grammars#naming_conventions
DATA = """
    comment
        line
            double-slash
            double-dash
            number-sign
            percentage
            semi-colon
        block
            documentation

    constant
        numeric
            integer
                binary
                octal
                decimal
                hexadecimal
                other
            float
                binary
                octal
                decimal
                hexadecimal
                other
            complex
                real
                imaginary
        character
            escape
        language
        other
            placeholder

    entity
        name
            class
                forward-decl
            struct
            enum
            union
            trait
            interface
            impl
            type
            function
                constructor
                destructor
            namespace
            constant
            label
            section
            tag
        other
            inherited-class
            attribute-name

    invalid
        illegal
        deprecated

    keyword
        context
            block
            resource
        control
            conditional
                case
                else
                elseif
                end
                if
                select
                switch
            exception
                assert
                catch
                defer
                end
                finally
                try
            flow
                await
                break
                continue
                goto
                panic
                return
                throw
                yield
            loop
                do-while
                end
                for
                repeat-until
                while
            import
        declaration
            class
            enum
            function
            interface
            impl
            struct
            trait
            union
        import
            from
        operator
            assignment
            arithmetic
            bitwise
            comparison
            logical
            word
        other

    markup
        heading
        list
            numbered
            unnumbered
        bold
        italic
        underline
            link
        inserted
        deleted
        quote
        raw
            inline
            block
        info
        warning
        error
        other

    meta
        class
        struct
        enum
        union
        trait
        interface
        impl
        type
        function
            parameters
            return-type
        namespace
        preprocessor
        annotation
            identifier
            parameters
        path
        function-call
        block
        braces
        group
        parens
        brackets
        generic
        tag
        paragraph
        toc-list
        string
        interpolation
        sequence
        mapping
            key
            value
        set

    punctuation
        definition
            annotation
                begin
                end
            string
                begin
                end
            comment
                begin
                end
            keyword
                begin
                end
            generic
                begin
                end
            placeholder
                begin
                end
            variable
                begin
                end
        section
            block
                begin
                end
            braces
                begin
                end
            group
                begin
                end
            parens
                begin
                end
            brackets
                begin
                end
            sequence
                begin
                end
            mapping
                begin
                end
            set
                begin
                end
            interpolation
                begin
                end
        separator
            continuation
            sequence
            mapping
                key-value
                pair
            decimal
        terminator
        accessor
            arrow
            dot
            double-colon
            fat-arrow
            colon
            backslash

    storage
        type
            function
            class
            struct
            enum
            union
            trait
            interface
            impl
        modifier

    string
        quoted
            single
            double
            triple
            other
        unquoted
        regexp
        other

    support
        constant
        function
        module
        type
        class
        other

    variable
        language
        parameter
        function
        annotation
        other
            constant
            member
            readwrite

    source
    text

    color
        bluish
        cyanish
        greenish
        orangish
        pinkish
        purplish
        redish
        yellowish
"""
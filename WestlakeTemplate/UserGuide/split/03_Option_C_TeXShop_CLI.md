# Option C: TeXShop or Command Line

Here we assume you know the default way to compile your `.tex` to `.pdf`.

However, for us there will be several special setting requirements:

1. **Change your compiler to XeLaTeX** (since we have a lot of Chinese Characters in the document):
   - Example: for TeXShop, go to **Settings** -> **Typeset**:

     ![TeXShop Settings Typeset 1](../images/image16.png)

     ![TeXShop Settings Typeset 2](../images/image17.png)

   - In **Default Command**, select **Command Listed Below** and set **XeLaTeX**.

2. **Configure BibTeX Engine:**
   - When you’re compiling your proposal, change your BibTeX Engine under **Settings** -> **Engine** to **`biber`**. (For compiling `thesis.tex` you should use `bibtex` by default) (Short reason if you wish to know: in proposal we have two local references, one after the literature review section, the other after the real proposal section, to reach that goal we use another engine for reference management, resulting in this change):

     ![TeXShop Engine Settings](../images/image18.png)

%%
%% This is file ‘wuthesis.cls'
%% based on the fduthesis template.
%%
%% Copyright (C) 2017--2023 by Xiangdong Zeng <xdzeng96@gmail.com>
%% Copyright (C) 2025 by Shi Liu
%%
%% This work may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either
%% version 1.3c of this license or (at your option) any later
%% version. The latest version of this license is in:
%%
%%       https://www.latex-project.org/lppl.txt
%%
%% and version 1.3c or later is part of all distributions of
%% LaTeX version 2008 or later.
%%
%% This work has the LPPL maintenance status `maintained'.
%%
%% The Current Maintainer of this work is Shi Liu <sliutheory@outlook.com>.
%%
%% This work is a derived work based on the fduthesis template
%% originally developed by Xiangdong Zeng.
%%
%% This work consists of the files:
%%       wuthesis.cls
%%       wuthesis.def
%%

\NeedsTeXFormat{LaTeX2e}[2020/10/01]
\GetIdInfo $Id: wuthesis.cls 0.1 2025-12-16 Shi Liu $
  {Thesis template for Westlake University}
\ProvidesExplClass{\ExplFileName}
  {\ExplFileDate}{\ExplFileVersion}{\ExplFileDescription}
\RequirePackage { xtemplate, l3keys2e }
\msg_new:nnn { wuthesis } { l3-too-old }
  {
    Package~ "#1"~ is~ too~ old. \\\\
    Please~ update~ an~ up-to-date~ version~ of~ the~ bundles \\
    "l3kernel"~ and~ "l3packages"~ using~ your~ TeX~ package \\
    manager~ or~ from~ CTAN.
  }
\clist_map_inline:nn { xtemplate, l3keys2e }
  {
    \@ifpackagelater {#1} { 2020/07/17 }
      { } { \msg_error:nnn { wuthesis } { l3-too-old } {#1} }
  }
\msg_new:nnn { wuthesis } { unsupported-engine }
  {
    The~ wuthesis~ class~ requires~ either~ XeTeX~ or~ LuaTeX. \\\\
    "#1"~ is~ not~ supported~ at~ present.~ You~ must~ change \\
    your~ typesetting~ engine~ to~ "xelatex"~ or~ "lualatex".
  }
\sys_if_engine_xetex:F
  {
    \sys_if_engine_luatex:F
      {
        \msg_fatal:nnx { wuthesis } { unsupported-engine }
          { \c_sys_engine_str }
      }
  }
\box_new:N   \l__wu_tmpa_box
\clist_new:N \l__wu_tmpa_clist
\dim_new:N   \l__wu_tmpa_dim
\skip_new:N  \l__wu_tmpa_skip
\tl_new:N    \l__wu_tmpa_tl
\tl_new:N    \l__wu_tmpb_tl
\tl_new:N \g__wu_thesis_type_tl
\clist_new:N \g__wu_to_ctexbook_clist
\clist_new:N \g__wu_to_hyperref_clist
\bool_new:N \g__wu_twoside_bool
\bool_set_true:N \g__wu_twoside_bool
\bool_new:N \g__wu_draft_bool
\tl_new:N \g__wu_config_tl
\cs_generate_variant:Nn \file_input:n          { V   }
\cs_generate_variant:Nn \int_to_arabic:n       { v   }
\cs_generate_variant:Nn \keys_define:nn        { nx  }
\cs_generate_variant:Nn \prop_item:Nn          { No  }
\cs_generate_variant:Nn \regex_replace_all:nnN { nnc }
\prg_generate_conditional_variant:Nnn \tl_if_eq:nn { Vn } { T, TF }
\cs_new:Npn \__wu_quad:  { \skip_horizontal:n { 1 em } }
\cs_new:Npn \__wu_qquad: { \skip_horizontal:n { 2 em } }
\cs_new_protected:Npn \__wu_vspace:N #1
  {
    \dim_set_eq:NN \l__wu_tmpa_dim \prevdepth
    \hrule height \c_zero_dim
    \nobreak
    \skip_vertical:N #1
    \skip_vertical:N \c_zero_skip
    \dim_set_eq:NN \prevdepth \l__wu_tmpa_dim
  }
\cs_new_protected:Npn \__wu_vspace:n #1
  {
    \skip_set:Nn \l__wu_tmpa_skip {#1}
    \__wu_vspace:N \l__wu_tmpa_skip
  }
\cs_generate_variant:Nn \__wu_vspace:N { c }
\cs_new:Npn \__wu_symbol:n #1 { \tex_char:D #1 \scan_stop: }
\cs_new:Npn \__wu_arabic:n #1
  { \int_to_arabic:v { c@ #1 } }
\cs_new_protected:Npn \__wu_gadd_ltxhook:nn #1#2
  { \hook_gput_code:nnn {#1} { . } {#2} }
\hook_gset_rule:nnnn { begindocument/before } { . } { < } { xeCJK }
\cs_new_protected:Npn \__wu_patch_cmd:Nnn #1#2#3
  {
    \ctex_patch_cmd_once:NnnnTF #1 { } {#2} {#3}
      { } { \ctex_patch_failure:N #1 }
  }
\cs_new_protected:Npn \__wu_appto_cmd:Nn #1#2
  {
    \ctex_appto_cmd:NnnTF #1 { } {#2}
      { } { \ctex_patch_failure:N #1 }
  }
\cs_new_protected:Npn \__wu_define_fn_style:nn #1#2
  { \tl_const:cn { c__wu_fn_style_ #1 _tl } {#2} }
\cs_new_protected:Npn \__wu_define_punct:nn #1#2
  { \tl_const:cn { c__wu_ #1 _tl } {#2} }
\cs_new_protected:Npn \__wu_define_name:nn #1#2
  { \tl_const:cn { c__wu_name_ #1 _tl } {#2} }
\cs_new_protected:Npn \__wu_define_name:nnn #1#2#3
  {
    \tl_const:cn { c__wu_name_ #1    _tl } {#2}
    \tl_const:cn { c__wu_name_ #1 _en_tl } {#3}
  }
\cs_new:Npn \__wu_msg_new:nn  { \msg_new:nnn      { wuthesis } }
\cs_new:Npn \__wu_error:n     { \msg_error:nn     { wuthesis } }
\cs_new:Npn \__wu_error:nn    { \msg_error:nnn    { wuthesis } }
\cs_new:Npn \__wu_error:nx    { \msg_error:nnx    { wuthesis } }
\cs_new:Npn \__wu_error:nnn   { \msg_error:nnnn   { wuthesis } }
\cs_new:Npn \__wu_error:nnnn  { \msg_error:nnnnn  { wuthesis } }
\cs_new:Npn \__wu_warning:n   { \msg_warning:nn   { wuthesis } }
\cs_new:Npn \__wu_warning:nn  { \msg_warning:nnn  { wuthesis } }
\cs_new:Npn \__wu_warning:nxx { \msg_warning:nnxx { wuthesis } }
\cs_new:Npn \__wu_info:nx     { \msg_info:nnx     { wuthesis } }
\keys_define:nn { wu / option }
  {
    type .choices:nn =
      { doctor, master, bachelor, proposal } % <--- 添加 proposal
      { \tl_set_eq:NN \g__wu_thesis_type_tl \l_keys_choice_tl },
    type .value_required:n = true,
    type .initial:n = bachelor,
    oneside .value_forbidden:n = true,
    twoside .value_forbidden:n = true,
    oneside .code:n =
      {
        \clist_gput_right:Nn \g__wu_to_ctexbook_clist { oneside }
        \bool_set_false:N    \g__wu_twoside_bool
      },
    twoside .code:n =
      {
        \clist_gput_right:Nn \g__wu_to_ctexbook_clist { twoside }
        \bool_set_true:N     \g__wu_twoside_bool
      },
    draft .choice:,
    draft / true  .code:n =
      {
        \bool_set_true:N     \g__wu_draft_bool
        \clist_gput_right:Nn \g__wu_to_ctexbook_clist { draft }
      },
    draft / false .code:n =
      { \bool_set_false:N    \g__wu_draft_bool },
    draft .default:n = true,
    draft .initial:n = false,
    config .tl_set:N = \g__wu_config_tl,
    unknown .code:n = { \__wu_error:n { unknown-option } }
  }
\__wu_msg_new:nn { unknown-option }
  { Class~ option~ "\l_keys_key_str"~ is~ unknown. }
\ProcessKeysOptions { wu / option }
\file_input:n { wuthesis.def }
\__wu_msg_new:nn { load-config-file }
  { You~ are~ loading~ config~ file~ "#1". }
\tl_if_empty:NF \g__wu_config_tl
  {
    \__wu_info:nx { load-config-file } { \g__wu_config_tl }
    \file_input:V \g__wu_config_tl
  }
\PassOptionsToClass
  {
    UTF8,
    heading    = true,
    fontset    = none,
    zihao      = -4,
    linespread = \c__wu_line_spread_fp,
    \g__wu_to_ctexbook_clist
  }
  { ctexbook }
\clist_map_inline:nn
  {
    { no-math           } { fontspec },
    { perpage           } { footmisc },
    { amsmath, thmmarks } { ntheorem }
  }
  { \PassOptionsToPackage #1 }
\LoadClass { ctexbook }
\RequirePackage
  {
    amsmath,
    unicode-math,
    geometry,
    fancyhdr,
    footmisc,
    ntheorem,
    graphicx,
    longtable,
    caption,
    xcolor
  }
\cs_new_protected:Npn \__wu_check_package:nnn #1#2#3
  {
    \@ifpackagelater {#1} {#2}
      { } { \__wu_error:nnnn { package-too-old } { Package } {#1} {#3} }
  }
\cs_new_protected:Npn \__wu_check_class:nnn #1#2#3
  {
    \@ifclasslater {#1} {#2}
      { } { \__wu_error:nnnn { package-too-old } { Class } {#1} {#3} }
  }
\__wu_msg_new:nn { package-too-old }
  {
    #1~ "#2"~ is~ too~ old. \\
    The~ wuthesis~ class~ only~ supports~ "#2" \\
    with~ a~ version~ higher~ than~ v#3. \\\\
    Please~ update~ an~ up-to-date~ version~ of~ it \\
    using~ your~ TeX~ package~ manager~ or~ from~ CTAN.
  }
\__wu_check_class:nnn { ctexbook } { 2021/03/14 } { 2.5.6 }
\sys_if_engine_xetex:T
  { \__wu_check_package:nnn { xeCJK } { 2020/05/01 } { 3.8.3 } }
\geometry
  {
    paper      = a4paper,
    vmargin    = 2.54 cm,
    hmargin    = 3.18 cm,
    headheight = 15 pt
  }
\bool_if:NT \g__wu_draft_bool { \geometry { showframe } }
\tl_new:N \g__wu_fontset_tl
\tl_new:N \g__wu_cjk_fontset_tl
\keys_define:nn { wu / style }
  {
    font .choices:nn =
      { garamond, libertinus, lm, palatino, times, times*, none }
      { \tl_set_eq:NN \g__wu_fontset_tl \l_keys_choice_tl },
    font .value_required:n = true,
  }
\keys_define:nn { wu / style }
  {
    cjk-font .choices:nn =
      { adobe, fandol, founder, mac, sinotype, sourcehan, windows, none }
      { \tl_set_eq:NN \g__wu_cjk_fontset_tl \l_keys_choice_tl },
    cjk-font .value_required:n = true,
  }
\cs_new_protected:Npn \__wu_setmainfont:nn #1#2
  { \__fontspec_main_setmainfont:nn {#2} {#1} }
\cs_new_protected:Npn \__wu_setsansfont:nn #1#2
  { \__fontspec_main_setsansfont:nn {#2} {#1} }
\cs_new_protected:Npn \__wu_setmonofont:nn #1#2
  { \__fontspec_main_setmonofont:nn {#2} {#1} }
\cs_new_protected:Npn \__wu_setmathfont:nn #1#2
  { \__um_setmathfont:nn {#2} {#1} }
\cs_new_protected:Npn \__wu_setCJKmainfont:nn #1#2
  { \__wu_set_family:xnn { \CJKrmdefault } {#2} {#1} }
\cs_new_protected:Npn \__wu_setCJKsansfont:nn #1#2
  { \__wu_set_family:xnn { \CJKsfdefault } {#2} {#1} }
\cs_new_protected:Npn \__wu_setCJKmonofont:nn #1#2
  { \__wu_set_family:xnn { \CJKttdefault } {#2} {#1} }
\cs_new_protected:Npn \__wu_set_cjk_font_kai:nn #1#2
  { \__wu_set_family:nnn { wu@kai } {#2} {#1} }
\cs_new_protected:Npn \wu@kai
  { \__wu_switch_family:n { wu@kai } }
\tl_const:Nn \__wu_cjk_font_options:
 { UprightFont = *, ItalicFont = *, AutoFakeBold = true }
\cs_new_protected:Npx \__wu_setCJKmainfont:n   #1
  { \__wu_setCJKmainfont:nn   {#1} { \__wu_cjk_font_options: } }
\cs_new_protected:Npx \__wu_setCJKsansfont:n   #1
  { \__wu_setCJKsansfont:nn   {#1} { \__wu_cjk_font_options: } }
\cs_new_protected:Npx \__wu_setCJKmonofont:n   #1
  { \__wu_setCJKmonofont:nn   {#1} { \__wu_cjk_font_options: } }
\cs_new_protected:Npx \__wu_set_cjk_font_kai:n #1
  { \__wu_set_cjk_font_kai:nn {#1} { \__wu_cjk_font_options: } }
\sys_if_engine_xetex:TF
  {
    \cs_new_eq:NN \__wu_set_family:nnn  \xeCJK_set_family:nnn
    \cs_new_eq:NN \__wu_switch_family:n \xeCJK_switch_family:n
  }
  {
    \cs_new_eq:NN \__wu_set_family:nnn  \ctex_ltj_set_family:nnn
    \cs_new_eq:NN \__wu_switch_family:n \ctex_ltj_switch_family:n
  }
\cs_generate_variant:Nn \__wu_set_family:nnn { x }
\cs_new_protected:Npn \__wu_set_font_helper:n #1
  {
    \exp_args:Nc \RenewDocumentCommand { set #1 font } { O { } m O { } }
      {
        \ctex_at_end_preamble:n
          { \use:c { __wu_set #1 font:nn } {##2} { ##1, ##3 } }
      }
  }
\clist_map_inline:nn { main, sans, mono, math }
  { \__wu_set_font_helper:n {#1} }
\clist_map_inline:nn { CJKmain, CJKsans, CJKmono }
  { \__wu_set_font_helper:n {#1} }
\cs_new_protected:Npn \__wu_load_font_garamond:
  {
    \__wu_setmainfont:nn { EBGaramond }
      {
        Extension      = .otf,
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Italic,
        BoldItalicFont = *-BoldItalic
      }
    \__wu_setsansfont:nn { LibertinusSans }
      {
        Extension      = .otf,
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Italic,
      }
    \__wu_setmonofont:nn { lmmonolt10 }
      {
        Extension      = .otf,
        UprightFont    = *-regular,
        BoldFont       = *-bold,
        ItalicFont     = *-oblique,
        BoldItalicFont = *-boldoblique
      }
    \__wu_setmathfont:nn { Garamond-Math.otf } { }
  }
\cs_new_protected:Npn \__wu_load_font_libertinus:
  {
    \__wu_setmainfont:nn { LibertinusSerif }
      {
        Extension      = .otf,
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Italic,
        BoldItalicFont = *-BoldItalic,
      }
    \__wu_setsansfont:nn { LibertinusSans }
      {
        Extension      = .otf,
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Italic,
      }
    \__wu_setmonofont:nn { lmmonolt10 }
      {
        Extension      = .otf,
        UprightFont    = *-regular,
        BoldFont       = *-bold,
        ItalicFont     = *-oblique,
        BoldItalicFont = *-boldoblique
      }
    \__wu_setmathfont:nn { LibertinusMath-Regular.otf } { }
  }
\cs_new_protected:Npn \__wu_load_font_lm:
  { \__wu_setmathfont:nn { latinmodern-math.otf } { } }
\cs_new_protected:Npn \__wu_load_font_palatino:
  {
    \__wu_setmainfont:nn { texgyrepagella }
      {
        Extension      = .otf,
        UprightFont    = *-regular,
        BoldFont       = *-bold,
        ItalicFont     = *-italic,
        BoldItalicFont = *-bolditalic
      }
    \__wu_setsansfont:nn { LibertinusSans }
      {
        Extension      = .otf,
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Italic,
        Scale          = MatchUppercase,
      }
    \__wu_setmonofont:nn { lmmonolt10 }
      {
        Extension      = .otf,
        UprightFont    = *-regular,
        BoldFont       = *-bold,
        ItalicFont     = *-oblique,
        BoldItalicFont = *-boldoblique
      }
    \__wu_setmathfont:nn { texgyrepagella-math.otf } { }
  }
\cs_new_protected:Npn \__wu_load_font_times:
  {
    \__wu_setmainfont:nn { XITS }
      {
        Extension      = .otf,
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Italic,
        BoldItalicFont = *-BoldItalic,
      }
    \__wu_setsansfont:nn { texgyreheros }
      {
        Extension      = .otf,
        UprightFont    = *-regular,
        BoldFont       = *-bold,
        ItalicFont     = *-italic,
        BoldItalicFont = *-bolditalic
      }
    \__wu_setmonofont:nn { texgyrecursor }
      {
        Extension      = .otf,
        UprightFont    = *-regular,
        BoldFont       = *-bold,
        ItalicFont     = *-italic,
        BoldItalicFont = *-bolditalic,
        Ligatures      = CommonOff
      }
    \__wu_setmathfont:nn { XITSMath-Regular.otf }
      { BoldFont = XITSMath-Bold.otf }
  }
\cs_new_protected:cpn { __wu_load_font_ times* : }
  {
    \__wu_setmainfont:nn { Times~ New~ Roman    } { }
    \__wu_setsansfont:nn { Arial                } { }
    \__wu_setmonofont:nn { Courier~ New         } { }
    \__wu_setmathfont:nn { XITSMath-Regular.otf }
      { BoldFont = XITSMath-Bold.otf }
  }
\cs_new_protected:Npn \__wu_load_cjk_font_adobe:
  {
    \__wu_setCJKmainfont:n   { AdobeSongStd-Light       }
    \__wu_setCJKsansfont:n   { AdobeHeitiStd-Regular    }
    \__wu_setCJKmonofont:n   { AdobeFangsongStd-Regular }
    \__wu_set_cjk_font_kai:n { AdobeKaitiStd-Regular    }
  }
\cs_new_protected:Npn \__wu_load_cjk_font_fandol:
  {
    \__wu_setCJKmainfont:nn   { FandolSong }
      {
        Extension      = .otf,
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Regular,
        BoldItalicFont = *-Bold
      }
    \__wu_setCJKsansfont:nn   { FandolHei  }
      {
        Extension      = .otf,
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Regular,
        BoldItalicFont = *-Bold
      }
    \__wu_setCJKmonofont:nn   { FandolFang }
      {
        Extension      = .otf,
        UprightFont    = *-Regular,
        BoldFont       = *-Regular,
        ItalicFont     = *-Regular,
        BoldItalicFont = *-Regular
      }
    \__wu_set_cjk_font_kai:nn { FandolKai  }
      {
        Extension      = .otf,
        UprightFont    = *-Regular,
        BoldFont       = *-Regular,
        ItalicFont     = *-Regular,
        BoldItalicFont = *-Regular
      }
  }
\cs_new_protected:Npn \__wu_load_cjk_font_founder:
  {
    \__wu_setCJKmainfont:n   { FZShuSong-Z01  }
    \__wu_setCJKsansfont:n   { FZHei-B01      }
    \__wu_setCJKmonofont:n   { FZFangSong-Z02 }
    \__wu_set_cjk_font_kai:n { FZKai-Z03      }
  }
\cs_new_protected:Npn \__wu_load_cjk_font_mac:
  {
    \__wu_setCJKmainfont:nn   { STSongti-SC }
      {
        UprightFont    = *-Light,
        BoldFont       = *-Bold,
        ItalicFont     = *-Light,
        BoldItalicFont = *-Bold
      }
    \__wu_setCJKsansfont:nn   { STHeitiSC   }
      {
        UprightFont    = *-Medium,
        BoldFont       = *-Medium,
        ItalicFont     = *-Medium,
        BoldItalicFont = *-Medium
      }
    \__wu_setCJKmonofont:n    { STFangsong  }
    \__wu_set_cjk_font_kai:nn { STKaitiSC   }
      {
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Regular,
        BoldItalicFont = *-Bold
      }
  }
\cs_new_protected:Npn \__wu_load_cjk_font_sinotype:
  {
    \__wu_setCJKmainfont:n   { STSong     }
    \__wu_setCJKsansfont:n   { STHeiti    }
    \__wu_setCJKmonofont:n   { STFangsong }
    \__wu_set_cjk_font_kai:n { STKaiti    }
  }
\cs_new_protected:Npn \__wu_load_cjk_font_sourcehan:
  {
    \__wu_setCJKmainfont:nn { SourceHanSerifSC }
      {
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Regular,
        BoldItalicFont = *-Bold
      }
    \__wu_setCJKsansfont:nn { SourceHanSansSC  }
      {
        UprightFont    = *-Regular,
        BoldFont       = *-Bold,
        ItalicFont     = *-Regular,
        BoldItalicFont = *-Bold
      }
    \__wu_warning:n { source-han }
  }
\__wu_msg_new:nn { source-han }
  { Font~ set~ "sourcehan"~ does~ not~ contain~ kaiti~ and~ fangsong. }
\cs_new_protected:Npn \__wu_load_cjk_font_windows:
  {
    \__wu_setCJKmainfont:n   { SimSun   }
    \__wu_setCJKsansfont:n   { SimHei   }
    \__wu_setCJKmonofont:n   { FangSong }
    \__wu_set_cjk_font_kai:n { KaiTi    }
  }
\cs_new_protected:Npn \__wu_load_font:
  {
    \use:c { __wu_load_font_     \g__wu_fontset_tl     : }
    \use:c { __wu_load_cjk_font_ \g__wu_cjk_fontset_tl : }
  }
\ctex_at_end_preamble:n { \__wu_load_font: }
\keys_set:nn { unicode-math }
  {
    math-style = ISO,
    bold-style = ISO,
  }
\keys_define:nn { wu / style }
  {
    font-size .choice:,
    font-size .value_required:n = true,
    font-size / -4 .code:n = { },
    font-size /  5 .code:n = { \ctex_file_input:n { ctex-c5size.clo } },
    fullwidth-stop .choice:,
    fullwidth-stop .value_required:n = true,
    fullwidth-stop / catcode .code:n =
      { \__wu_set_fullwidth_stop_catcode: },
    fullwidth-stop / mapping .code:n =
      {
        \sys_if_engine_xetex:TF
          {
            \clist_gset:Nn \g__xeCJK_default_features_clist
              { Mapping = fullwidth-stop }
          }
          {
            \sys_if_engine_luatex:T
              {
                \__wu_warning:n { mapping-not-available }
                \__wu_set_fullwidth_stop_catcode:
              }
          }
      },
    fullwidth-stop / false .code:n = { }
  }
\__wu_msg_new:nn { mapping-not-available }
  {
    Option~ "fullwidth-stop = mapping"~ is~ not~ available~ in~ LuaTeX. \\
    "fullwidth-stop = catcode"~ will~ be~ set~ instead.
  }
\cs_new:Npn \__wu_set_fullwidth_stop_catcode:
  {
    \char_set_active_eq:NN ^^^^3002 \c__wu_fwid_full_stop_tl
    \char_set_catcode_active:N ^^^^3002
    \clist_map_inline:nn
      { \c__wu_orig_decl_text_tl, \c__wu_auth_decl_text_tl }
      { \tl_set_rescan:Nno ##1 { } {##1} }
  }
\DeclareEmphSequence
  {
    \itshape \wu@kai,
    \upshape \CJKfamily { \CJKfamilydefault },
  }
\fancyhf { }
\cs_new_protected:Npn \__wu_fancy_head:nn #1#2
  {
    \fancyhead [#1]
      {
        \zihao { 5 }
        \CJKfamily { \CJKrmdefault }
        \nouppercase {#2}
      }
  }
\bool_if:NTF \g__wu_twoside_bool
  {
    \__wu_fancy_head:nn { EC } { \leftmark  }
    \__wu_fancy_head:nn { OC } { \leftmark }
  }
  {
    \__wu_fancy_head:nn { C } { \leftmark }
  }
\fancyfoot [ C ] { \small \thepage }
\RenewDocumentCommand \cleardoublepage { }
  {
    \clearpage
    \bool_if:NT \g__wu_twoside_bool
      {
        \int_if_odd:nF \c@page
          { \hbox:n { } \thispagestyle { empty } \newpage }
      }
  }
\pagestyle { fancy }
% 让 chapter 首页也使用 fancy 页眉
\cs_set_eq:NN \ps@plain \ps@fancy
\keys_set:nn { ctex }
  {
    chapter =
      {
        format      = \huge \normalfont \sffamily \centering,
        beforeskip  = 50 pt,
        afterskip   = 40 pt,
        number      = \__wu_arabic:n { chapter },
        fixskip     = true
      },
    section =
      {
        format      = \Large \normalfont \sffamily \raggedright,
        beforeskip  = 3.5 ex plus 1.0 ex minus 0.2 ex,
        afterskip   = 2.7 ex plus 0.5 ex,
        fixskip     = true
      },
    subsection =
      {
        format      = \large \normalfont \sffamily \raggedright,
        beforeskip  = 3.25 ex plus 1.0 ex minus 0.2 ex,
        afterskip   = 2.5  ex plus 0.3 ex,
        fixskip     = true
      }
  }
% Ensure chapter-opening pages have both left and right header marks.
\cs_set_protected:Npn \chaptermark #1
  {
    \markboth {#1} {#1}
  }
\cs_new_protected:Npn \__wu_sanitize_chapter_title:n #1
  {
    \tl_clear:N \l__wu_tmpa_tl
    \tl_set:No \l__wu_tmpa_tl {#1}
    \tl_remove_all:Nn \l__wu_tmpa_tl { \quad }
  }
\cs_new_protected:Npn \__wu_chapter:n #1
  {
    \__wu_sanitize_chapter_title:n {#1}
    \group_begin:
      \ctexset { chapter / numbering = false }
      \chapter [ \l__wu_tmpa_tl ] {#1}
    \group_end:
    \__wu_chapter_header:n {#1}
  }
\cs_generate_variant:Nn \__wu_chapter:n { V }
\cs_new_protected:Npn \__wu_chapter_no_toc:n #1
  {
    \chapter * {#1}
    \__wu_sanitize_chapter_title:n {#1}
    \pdfbookmark [0] { \l__wu_tmpa_tl } { toc }
    \__wu_chapter_header:n {#1}
  }
\cs_generate_variant:Nn \__wu_chapter_no_toc:n { V }
\cs_new_protected:Npn \__wu_chapter_header:n #1
  {
    \bool_if:NTF \g__wu_twoside_bool
      { \markboth {#1} {#1} }
      { \markboth { \hfill #1 \hfill } { } }
  }
\clist_map_inline:nn
  {
    { plain           } { plain           },
    { libertinus      } { libertinus      },
    { libertinus_neg  } { libertinus*     },
    { libertinus_sans } { libertinus-sans },
    { pifont          } { pifont          },
    { pifont_neg      } { pifont*         },
    { pifont_sans     } { pifont-sans     },
    { pifont_sans_neg } { pifont-sans*    },
    { xits            } { xits            },
    { xits_sans       } { xits-sans       },
    { xits_sans_neg   } { xits-sans*      }
  }
  { \__wu_define_fn_style:nn #1 }
\tl_new:N \l__wu_fn_style_tl
\keys_define:nn { wu / style }
  {
    footnote-style .choices:nn =
      {
        plain,
        libertinus, libertinus*, libertinus-sans,
        pifont,     pifont*,     pifont-sans,     pifont-sans*,
        xits,                    xits-sans,       xits-sans*
      }
      {
        \tl_gset_eq:NN \l__wu_fn_style_tl \l_keys_choice_tl
        \int_compare:nT { 5 <= \l_keys_choice_int <= 8 }
          { \RequirePackage { pifont } }
      },
    footnote-style .value_required:n = true
  }
\cs_new:Npn \__wu_fn_symbol_libertinus:n #1
  {
    \int_compare:nTF { #1 >= 21 }
      {
        \int_compare:nTF { #1 >= 47 }
          { \__wu_symbol:n { \int_eval:n { "24B6 - 47 + #1 } } }
          { \__wu_symbol:n { \int_eval:n { "24D0 - 21 + #1 } } }
      }
      { \__wu_symbol:n { \int_eval:n { "2460 - 1 + #1 } } }
  }
\cs_new:Npn \__wu_fn_symbol_libertinus_neg:n #1
  {
    \int_compare:nTF { #1 >= 11 }
      { \__wu_symbol:n { \int_eval:n { "24EB - 11 + #1 } } }
      { \__wu_symbol:n { \int_eval:n { "2776 -  1 + #1 } } }
  }
\cs_new:Npn \__wu_fn_symbol_pifont:n #1
  { \ding { \int_eval:n { 171 + #1 } } }
\cs_new:Npn \__wu_fn_symbol_pifont_neg:n #1
  { \ding { \int_eval:n { 181 + #1 } } }
\cs_new:Npn \__wu_fn_symbol_pifont_sans:n #1
  { \ding { \int_eval:n { 191 + #1 } } }
\cs_new:Npn \__wu_fn_symbol_pifont_sans_neg:n #1
  { \ding { \int_eval:n { 201 + #1 } } }
\cs_new:Npn \__wu_fn_symbol_xits:n #1
  {
    \int_compare:nTF { #1 >= 10 }
      {
        \int_compare:nTF { #1 >= 36 }
          { \__wu_symbol:n { \int_eval:n { "24B6 - 36 + #1 } } }
          { \__wu_symbol:n { \int_eval:n { "24D0 - 10 + #1 } } }
      }
      { \__wu_symbol:n { \int_eval:n { "2460 - 1 + #1 } } }
  }
\cs_new:Npn \__wu_fn_symbol_xits_sans:n #1
  { \__wu_symbol:n { \int_eval:n { "2780 - 1 + #1 } } }
\cs_new:Npn \__wu_fn_symbol_xits_sans_neg:n #1
  { \__wu_symbol:n { \int_eval:n { "278A - 1 + #1 } } }
\cs_set:Npn \thefootnote { \wu_footnote_number:N \c@footnote }
\cs_new:Npn \wu_footnote_number:N #1
  {
    \tl_case:NnF \l__wu_fn_style_tl
      {
        \c__wu_fn_style_plain_tl
          { \int_use:N #1 }
        \c__wu_fn_style_libertinus_tl
          {
            \fontspec { LibertinusSerif-Regular.otf }
            \__wu_fn_symbol_libertinus:n {#1}
          }
        \c__wu_fn_style_libertinus_neg_tl
          {
            \fontspec { LibertinusSerif-Regular.otf }
            \__wu_fn_symbol_libertinus_neg:n {#1}
          }
        \c__wu_fn_style_libertinus_sans_tl
          {
            \fontspec { LibertinusSans-Regular.otf }
            \__wu_fn_symbol_libertinus:n {#1}
          }
        \c__wu_fn_style_pifont_tl
          { \__wu_fn_symbol_pifont:n {#1} }
        \c__wu_fn_style_pifont_neg_tl
          { \__wu_fn_symbol_pifont_neg:n {#1} }
        \c__wu_fn_style_pifont_sans_tl
          { \__wu_fn_symbol_pifont_sans:n {#1} }
        \c__wu_fn_style_pifont_sans_neg_tl
          { \__wu_fn_symbol_pifont_sans_neg:n {#1} }
        \c__wu_fn_style_xits_tl
          {
            \fontspec { XITS-Regular.otf }
            \__wu_fn_symbol_xits:n {#1}
          }
        \c__wu_fn_style_xits_sans_tl
          {
            \fontspec { XITS-Regular.otf }
            \__wu_fn_symbol_xits_sans:n {#1}
          }
        \c__wu_fn_style_xits_sans_neg_tl
          {
            \fontspec { XITS-Regular.otf }
            \__wu_fn_symbol_xits_sans_neg:n {#1}
          }
      }
      { \int_use:N #1 }
  }
\cs_set:Npn \@makefntext #1
  {
    \mode_leave_vertical:
    \hbox_to_wd:nn { 1.5 em } { \@thefnmark \hfil }
    #1
  }
\clist_const:Nn \c__wu_thm_style_plain_clist
  { plain, margin, change }
\clist_const:Nn \c__wu_thm_style_break_clist
  { break, marginbreak, changebreak }
\tl_new:N \l__wu_thm_style_tl
\tl_new:N \l__wu_thm_header_font_tl
\tl_new:N \l__wu_thm_body_font_tl
\tl_new:N \l__wu_thm_qed_tl
\tl_new:N \l__wu_thm_counter_tl
\keys_define:nn { wu / theorem }
  {
    style       .tl_set:N  = \l__wu_thm_style_tl,
    header-font .tl_set:N  = \l__wu_thm_header_font_tl,
    body-font   .tl_set:N  = \l__wu_thm_body_font_tl,
    qed         .tl_set:N  = \l__wu_thm_qed_tl,
    counter     .tl_set:N  = \l__wu_thm_counter_tl
  }
\cs_new_eq:NN \__wu_thm_ntheorem_style:n \theoremstyle
\cs_new_eq:NN \__wu_thm_ntheorem_new:w   \newtheorem
\DeclareDocumentCommand \newtheorem { s o m m }
  {
    \IfBooleanTF {#1}
      { \tl_set:Nn \l__wu_thm_qed_tl { \ensuremath { \QED } } }
      { \tl_set:Nn \l__wu_thm_qed_tl { } }
    \tl_set:Nn \l__wu_thm_style_tl { plain }
    \IfValueT {#2} { \keys_set:nn { wu / theorem } {#2} }
    \wu_thm_set_header_font:V \l__wu_thm_header_font_tl
    \wu_thm_set_body_font:V   \l__wu_thm_body_font_tl
    \wu_thm_set_qed:V         \l__wu_thm_qed_tl
    \IfBooleanTF {#1}
      {
        \clist_if_in:nVF { plain, break } \l__wu_thm_style_tl
          {
            \clist_if_in:NVTF
              \c__wu_thm_style_plain_clist \l__wu_thm_style_tl
              { \__wu_thm_redefine_style:n { plain } }
              {
                \clist_if_in:NVTF
                  \c__wu_thm_style_break_clist \l__wu_thm_style_tl
                  { \__wu_thm_redefine_style:n { break } }
                  {
                    \__wu_error:nx { unknown-theorem-style }
                      { \l__wu_thm_style_tl }
                  }
              }
          }
        \tl_put_left:Nn \l__wu_thm_style_tl { nonumber }
        \wu_thm_new_no_number:Vxx \l__wu_thm_style_tl {#3} {#4}
      }
      {
        \clist_clear:N \l__wu_tmpa_clist
        \clist_concat:NNN \l__wu_tmpa_clist
          \c__wu_thm_style_plain_clist \c__wu_thm_style_break_clist
        \clist_if_in:NVF \l__wu_tmpa_clist \l__wu_thm_style_tl
          {
            \__wu_error:nx { unknown-theorem-style }
              { \l__wu_thm_style_tl }
          }
        \wu_thm_new:VVxx \l__wu_thm_style_tl \l__wu_thm_counter_tl
          {#3} {#4}
      }
  }
\cs_new:Npn \__wu_thm_redefine_style:n #1
  {
    \__wu_warning:nxx { redefine-theorem-style }
      {#1} { \l__wu_thm_style_tl }
    \tl_set:Nn \l__wu_thm_style_tl {#1}
  }
\__wu_msg_new:nn { redefine-theorem-style }
  { Theorem~ style~ "#2"~ will~ be~ redefined~ as~ "#1". }
\__wu_msg_new:nn { unknown-theorem-style }
  { Theorem~ style~ "#1"~ is~ unknown. }
\cs_new:Npn \wu_thm_new:nnnn #1#2#3#4
  {
    \__wu_thm_ntheorem_style:n {#1}
    \__wu_thm_ntheorem_new:w   {#3} {#4} [#2]
  }
\cs_generate_variant:Nn \wu_thm_new:nnnn { VVxx }
\cs_new:Npn \wu_thm_new_no_number:nnn #1#2#3
  {
    \__wu_thm_ntheorem_style:n {#1}
    \__wu_thm_ntheorem_new:w   {#2} {#3}
  }
\cs_generate_variant:Nn \wu_thm_new_no_number:nnn { Vxx }
\cs_new:Npn \wu_thm_set_qed:n         #1 { \theoremsymbol     {#1} }
\cs_new:Npn \wu_thm_set_header_font:n #1 { \theoremheaderfont {#1} }
\cs_new:Npn \wu_thm_set_body_font:n   #1 { \theorembodyfont   {#1} }
\cs_generate_variant:Nn \wu_thm_set_qed:n         { V }
\cs_generate_variant:Nn \wu_thm_set_header_font:n { V }
\cs_generate_variant:Nn \wu_thm_set_body_font:n   { V }
\captionsetup [ figure ] { font = small,         labelsep = quad }
\captionsetup [ table  ] { font = { small, sf }, labelsep = quad }
\cs_set:Npn \thefigure
  { \thechapter - \__wu_arabic:n { figure } }
\cs_set:Npn \thetable
  { \thechapter - \__wu_arabic:n { table  } }
\clist_map_inline:nn
  {
    title, date, author, supervisor, department, major, student_id,
    school_id, clc, jel
  }
  { \tl_new:c { l__wu_info_ #1 _tl } }
\clist_new:N \l__wu_info_instructors_clist
\clist_new:N \l__wu_info_keywords_clist
\clist_map_inline:nn
  { title, author, supervisor, department, major }
  { \tl_new:c { l__wu_info_ #1 _en_tl } }
\clist_new:N \l__wu_info_keywords_en_clist
\tl_new:N \l__wu_info_degree_type_tl
\tl_new:N \l__wu_info_title_sanitized_tl
\tl_new:N \l__wu_info_title_en_sanitized_tl
\cs_new_protected:Npn \__wu_set_title:nn #1#2
  {
    \tl_set:cn { l__wu_info_ #1 _tl           } {#2}
    \tl_set:cn { l__wu_info_ #1 _sanitized_tl } {#2}
    \tl_replace_all:cnn { l__wu_info_ #1 _sanitized_tl } { \\ } { ~ }
    \regex_replace_all:nnc
      { \s+ } { \ }
      { l__wu_info_ #1 _sanitized_tl }
    \regex_replace_all:nnc
      { ([\x{4e00}-\x{9fff}]) \s+ ([\x{4e00}-\x{9fff}]) } { \1 \2 }
      { l__wu_info_ #1 _sanitized_tl }
  }
\keys_define:nn { wu / info }
  {
    degree      .choices:nn  =
      { academic, professional }
      { \tl_set_eq:NN \l__wu_info_degree_type_tl \l_keys_choice_tl },
    degree      .value_required:n = true,
    title       .code:n      = { \__wu_set_title:nn { title    } {#1} },
    title*      .code:n      = { \__wu_set_title:nn { title_en } {#1} },
    date        .tl_set:N    = \l__wu_info_date_tl,
    author      .tl_set:N    = \l__wu_info_author_tl,
    author*     .tl_set:N    = \l__wu_info_author_en_tl,
    supervisor  .tl_set:N    = \l__wu_info_supervisor_tl,
    supervisor*  .tl_set:N    = \l__wu_info_supervisor_en_tl,
    instructors .clist_set:N = \l__wu_info_instructors_clist,
    department  .tl_set:N    = \l__wu_info_department_tl,
    department*  .tl_set:N    = \l__wu_info_department_en_tl,
    major       .tl_set:N    = \l__wu_info_major_tl,
    major*       .tl_set:N    = \l__wu_info_major_en_tl,
    student-id  .tl_set:N    = \l__wu_info_student_id_tl,
    school-id   .tl_set:N    = \l__wu_info_school_id_tl,
    keywords    .clist_set:N = \l__wu_info_keywords_clist,
    keywords*   .clist_set:N = \l__wu_info_keywords_en_clist,
    clc         .tl_set:N    = \l__wu_info_clc_tl,
    jel         .tl_set:N    = \l__wu_info_jel_tl
  }
\tl_new:N    \l__wu_cover_logo_tl
\clist_new:N \l__wu_cover_logo_size_clist
\keys_define:nn { wu / style }
  {
    logo      .tl_set:N    = \l__wu_cover_logo_tl,
    logo-size .clist_set:N = \l__wu_cover_logo_size_clist
  }
\tl_new:N \l__wu_info_secret_level_tl
\keys_define:nn { wu / info }
  {
    secret-level .choices:nn  =
      { none, i, ii, iii }
      { \tl_set_eq:NN \l__wu_info_secret_level_tl \l_keys_choice_tl },
    secret-level .value_required:n = true,
    secret-year  .tl_set:N = \l__wu_info_secret_year_tl
  }
\cs_new_protected:Npn \__wu_spread_box:nn #1#2
  {
    \mode_leave_vertical:
    \hbox_to_wd:nn {#1} { \tl_map_inline:nn {#2} { ##1 \hfil } \unskip }
  }
\cs_generate_variant:Nn \__wu_spread_box:nn { no }
\cs_new_protected:Npn \__wu_center_box:nn #1#2
  {
    \mode_leave_vertical:
    \hbox_to_wd:nn {#1} { \hfil #2 \hfil }
  }
\cs_generate_variant:Nn \__wu_center_box:nn { Vn }
\cs_new:Npn \__wu_fixed_width_box:nn #1#2
  { \parbox {#1} {#2} }
\cs_new:Npn \__wu_fixed_width_center_box:nn #1#2
  { \parbox {#1} { \centering #2 } }
\cs_new:Npn \__wu_get_text_width:Nn #1#2
  {
    \hbox_set:Nn \l__wu_tmpa_box {#2}
    \dim_set:Nn #1 { \box_wd:N \l__wu_tmpa_box }
  }
\cs_generate_variant:Nn \__wu_get_text_width:Nn { NV }
\cs_new:Npn \__wu_blank_underline:n #1
  { \rule [ -0.5 ex ] {#1} { 0.4 pt } }
\cs_new:Npn \__wu_line_spread:N #1
  { \linespread { \fp_use:N #1 } \selectfont }
\cs_new:Npn \__wu_line_spread:n #1
  { \linespread {#1} \selectfont }
\cs_new_protected:Npn \__wu_cover_id:
  {
    \tl_if_eq:NnTF \l__wu_info_secret_level_tl { none }
      { \__wu_cover_id_tabular:n { } }
      { \__wu_cover_id_tabular:n { \__wu_cover_secret: \\ } }
  }
\cs_new_protected:Npn \__wu_cover_id_tabular:n #1
  {
    \exp_args:Nnx \begin{tabular} { \c__wu_cover_id_align_tl }
      #1
      \__wu_cover_id_aux:n { school_id  } \\
      \__wu_cover_id_aux:n { student_id }
    \end{tabular}
  }
\cs_new:Npn \__wu_cover_id_aux:n #1
  {
    \tl_use:c { c__wu_name_ #1 _tl } &
    \tl_use:c { l__wu_info_ #1 _tl }
  }
\tl_const:Nn \c__wu_cover_id_align_tl
  { l @ { \c__wu_fwid_colon_tl } l @ { } }
\cs_new:Npn \__wu_cover_secret:
  {
    \multicolumn { 2 } { l }
      {
        \sffamily
        \c__wu_name_secret_level_tl
        \c__wu_fwid_colon_tl
        \prop_item:No \c__wu_secret_prop
          { \l__wu_info_secret_level_tl }
        \c__wu_name_secret_star_tl
        \l__wu_info_secret_year_tl
      }
  }
\cs_new_protected:Npn \__wu_cover_logo:
  {
    \clist_pop:NN   \l__wu_cover_logo_size_clist \l__wu_tmpa_tl
    \clist_pop:NNTF \l__wu_cover_logo_size_clist \l__wu_tmpb_tl
      {
        \tl_if_empty:NTF \l__wu_tmpa_tl
          { \includegraphics [ height = \l__wu_tmpb_tl ] }
          {
            \includegraphics
              [ width  = \l__wu_tmpa_tl, height = \l__wu_tmpb_tl ]
          }
      }
      { \includegraphics [ width = \l__wu_tmpa_tl ] }
    { \l__wu_cover_logo_tl }
  }
\cs_new_protected:Npn \__wu_cover_type:
  {
    \prop_get:NVN \c__wu_thesis_type_prop
      \g__wu_thesis_type_tl \l__wu_tmpa_tl
    \__wu_spread_box:no { 0.45 \textwidth } { \l__wu_tmpa_tl }
  }
\cs_new_protected:Npn \__wu_cover_degree:
  {
    \tl_if_eq:NnF \g__wu_thesis_type_tl { bachelor }
      {
        \c__wu_fwid_left_paren_tl
        \prop_item:No \c__wu_degree_type_prop
          { \l__wu_info_degree_type_tl }
        \c__wu_fwid_right_paren_tl
      }
  }
\cs_new_protected:Npn \__wu_cover_info:
  {
    \group_begin:
      %\zihao { 4 }
      \tl_if_eq:NnT \l__wu_info_degree_type_tl { professional }
        {
          \tl_set_eq:NN
            \c__wu_name_major_tl \c__wu_name_major_professional_tl
        }
      \clist_clear:N \l__wu_tmpa_clist
      \clist_map_inline:nn { department, major, author, supervisor}
        {
          \clist_gput_right:Nn \l__wu_tmpa_clist
            {
              \exp_args:Nx \__wu_cover_info_left:n
                { \tl_use:c { c__wu_name_ ##1 _tl } }
              &
              \tl_use:c { l__wu_info_ ##1 _tl }
            }
        }
      \exp_args:Nnx \begin{tabular} { \c__wu_cover_info_align_tl }
        \clist_use:Nn \l__wu_tmpa_clist { \\ [ 1 ex ] }
      \end{tabular}
    \group_end:
  }

% --- 新增：开题报告专用的信息列表 (包含学号) ---
\cs_new_protected:Npn \__wu_cover_info_proposal:
  {
    \group_begin:
      % 字体设置，根据模版看似是宋体或楷体，这里沿用正文设置或指定
      \zihao{4}
      \clist_clear:N \l__wu_tmpa_clist
      % 按照模版顺序：学院、专业、姓名、学号、导师
      \clist_map_inline:nn { department, major, author, supervisor }
        {
          \clist_gput_right:Nn \l__wu_tmpa_clist
            {
              \exp_args:Nx \__wu_cover_info_left:n
                { \tl_use:c { c__wu_name_ ##1 _tl } }
              &
              \tl_use:c { l__wu_info_ ##1 _tl }
            }
        }
      \exp_args:Nnx \begin{tabular} { \c__wu_cover_info_align_tl }
        \clist_use:Nn \l__wu_tmpa_clist { \\ [ 1.2 ex ] }
      \end{tabular}
    \group_end:
  }

% --- 新增：开题报告专用的导师签名框 ---
\cs_new_protected:Npn \__wu_cover_proposal_sign:
  {
    \clearpage
    \thispagestyle{empty}
    \group_begin:
      \centering
      % 设置表格行距，让内容不至于太拥挤
      \renewcommand{\arraystretch}{1.2}
      % 字号设置：正文小四，标题小三
      \zihao{-4} 
      
      % 定义表格：宽度为文本宽度的 95%，带边框
      \begin{tabular}{|p{0.95\textwidth}|}
        \hline
        % --- 顶部标题 ---
        \vspace{0.5em} % 顶部留白
        \noindent \zihao{-3} \bfseries  \ 导师对文献综述和开题报告的具体要求： \\
        
        % --- 中间空白区域 ---
        % 这里的 19cm 是根据 A4 纸减去页边距估算的，确保表格撑满页面
        % 如果编译后表格跑到了下一页，请适当减小这个数值（如 18cm）
         \vspace{0pt plus 1fill} 
        \vspace*{15cm} % 确保至少有 15cm 高，如果空间够大则自动拉伸
        
        % --- 底部签名区 ---
        \hfill 
        导师（签名）：\makebox[8em]{\hrulefill} \hspace{2em} \\
        \vspace{0.5em} % 签名和日期之间的间距
        \hfill 
        \makebox[3em]{\hrulefill} 年 \makebox[2em]{\hrulefill} 月 \makebox[2em]{\hrulefill} 日 \hspace{2em} \\
        \vspace{0.5em} % 底部留白
        \\ \hline
      \end{tabular}
    \group_end:
    \clearpage
  }
 
% 1. 定义英文版的信息列表 (English Info Table)
\cs_new_protected:Npn \__wu_cover_info_en:
  {
    \group_begin:
     % \zihao { 4 }
      \clist_clear:N \l__wu_tmpa_clist
      % 手动添加英文标签和对应的英文变量
      \clist_gput_right:Nn \l__wu_tmpa_clist { Department & \l__wu_info_department_en_tl }
      \clist_gput_right:Nn \l__wu_tmpa_clist { Major & \l__wu_info_major_en_tl }
      \clist_gput_right:Nn \l__wu_tmpa_clist { Author & \l__wu_info_author_en_tl }
      \clist_gput_right:Nn \l__wu_tmpa_clist { Supervisor & \l__wu_info_supervisor_en_tl }
      
      \exp_args:Nnx \begin{tabular} { \c__wu_cover_info_align_tl }
        \clist_use:Nn \l__wu_tmpa_clist { \\ [ 1 ex ] }
      \end{tabular}
    \group_end:
  }
  
 % 2. 定义英文版的论文类型 (English Thesis Type)
\cs_new_protected:Npn \__wu_cover_type_en:
  {
    \str_case:Vn \g__wu_thesis_type_tl
      {
        {doctor}   {Doctoral~ Dissertation}
        {master}   {Master's~ Thesis}
        {bachelor} {Undergraduate~Thesis/Capstone~Project}
      }
  }
% -------------------------------------------------------------  
\tl_const:Nn \c__wu_cover_info_align_tl
  { c @ { \c__wu_fwid_colon_tl } c }
\cs_new_protected:Npn \__wu_cover_info_left:n #1
  {
    \tl_if_eq:NnTF \l__wu_info_degree_type_tl { professional }
      { \__wu_spread_box:nn { 9 em } {#1} }
      { \__wu_spread_box:nn { 6 em } {#1} }
  }
\cs_new_protected:Npn \__wu_cover_signature:N #1
  {
    \clist_map_inline:Nn #1
      {
        ##1 \c__wu_fwid_colon_tl
        \__wu_blank_underline:n { 6 em }
        \__wu_quad:
      }
  }
\DeclareObjectType { wu / cover } { \c_zero_int }
\NewDocumentCommand \DeclareCoverTemplate { m m }
  { \wu_cover_declare_template:nn {#1} {#2} }
\cs_new_protected:Npn \wu_cover_declare_template:nn #1#2
  {
    \tl_set:Nn \l__wu_cover_template_tl {#1}
    \__wu_cover_declare_template_interface:nx {#1}
      {
        format      : tokenlist,
        top-skip    : skip,
        bottom-skip : skip,
        \clist_map_function:nN {#2} \__wu_cover_key_type:n
      }
    \tl_new:c   { l__wu_cover / #1 / format_tl   }
    \skip_new:c { l__wu_cover / #1 / top_skip    }
    \skip_new:c { l__wu_cover / #1 / bottom_skip }
    \clist_map_inline:nn {#2}
      {
        \tl_new:c   { l__wu_cover / #1 / ##1 / content_tl  }
        \tl_new:c   { l__wu_cover / #1 / ##1 / format_tl   }
        \skip_new:c { l__wu_cover / #1 / ##1 / bottom_skip }
      }
    \__wu_cover_declare_template_code:nxn {#1}
      {
        format      = \exp_not:c { l__wu_cover / #1 / format_tl   },
        top-skip    = \use:c     { l__wu_cover / #1 / top_skip    },
        bottom-skip = \use:c     { l__wu_cover / #1 / bottom_skip },
        \clist_map_function:nN {#2} \__wu_cover_key_binding:n
      }
      {
        \AssignTemplateKeys
        \tl_use:c       { l__wu_cover / #1 / format_tl }
        \__wu_vspace:c { l__wu_cover / #1 / top_skip  }
        \clist_map_inline:nn {#2}
          {
            \use:c { __wu_cover / #1 / ####1 / align:n }
              {
                \tl_use:c { l__wu_cover / #1 / ####1 / format_tl  }
                \tl_use:c { l__wu_cover / #1 / ####1 / content_tl }
                \par
              }
            \__wu_vspace:c { l__wu_cover / #1 / ####1 / bottom_skip }
          }
        \__wu_vspace:c { l__wu_cover / #1 / bottom_skip }
      }
  }
\tl_new:N \l__wu_cover_template_tl
\cs_new_protected:Npn \__wu_cover_declare_template_interface:nn #1#2
  { \DeclareTemplateInterface { wu / cover } {#1} { \c_zero_int } {#2} }
\cs_new_protected:Npn \__wu_cover_declare_template_code:nnn #1#2#3
  { \DeclareTemplateCode { wu / cover } {#1} { \c_zero_int } {#2} {#3} }
\cs_generate_variant:Nn \__wu_cover_declare_template_interface:nn { nx  }
\cs_generate_variant:Nn \__wu_cover_declare_template_code:nnn     { nxn }
\cs_new:Npn \__wu_cover_key_type:n #1
  {
    #1 / content     : tokenlist,
    #1 / format      : tokenlist,
    #1 / bottom-skip : skip,
    #1 / align       : choice { left, right, center, normal } = normal,
  }
\cs_new:Npn \__wu_cover_key_binding:n #1
  {
    #1 / content     =
      \exp_not:c
        { l__wu_cover / \l__wu_cover_template_tl / #1 / content_tl  },
    #1 / format      =
      \exp_not:c
        { l__wu_cover / \l__wu_cover_template_tl / #1 / format_tl   },
    #1 / bottom-skip =
      \exp_not:c
        { l__wu_cover / \l__wu_cover_template_tl / #1 / bottom_skip },
    #1 / align       =
      {
        left   =
          \exp_not:N \cs_set_protected:cpn
            { __wu_cover / \l__wu_cover_template_tl / #1 / align:n }
            \exp_not:n {##1}
            {
              \exp_not:n
                {
                  \group_begin:
                    \flushleft ##1 \endflushleft
                  \group_end:
                }
            },
        right  =
          \exp_not:N \cs_set_protected:cpn
            { __wu_cover / \l__wu_cover_template_tl / #1 / align:n }
            \exp_not:n {##1}
            {
              \exp_not:n
                {
                  \group_begin:
                    \flushright ##1 \endflushright
                  \group_end:
                }
            },
        center =
          \exp_not:N \cs_set_protected:cpn
            { __wu_cover / \l__wu_cover_template_tl / #1 / align:n }
            \exp_not:n {##1}
            {
              \exp_not:n
                {
                  \group_begin:
                    \center ##1 \endcenter
                  \group_end:
                }
            },
        normal =
          \exp_not:N \cs_set_protected:cpn
            { __wu_cover / \l__wu_cover_template_tl / #1 / align:n }
            \exp_not:n {##1}
            { \exp_not:n { \group_begin: ##1 \group_end: } }
      },
  }

% 原始的\makecoveri
% \NewDocumentCommand \makecoveri { }
%  {
%   % 1. 生成中文封面
%    \thispagestyle { empty }
%    \tl_set:Nn \thepage { A }
%    \UseInstance { wu / cover } { cover-i-default }
%    
%    % 2. 换页并生成英文封面
%    \newpage 
%    \thispagestyle { empty }
%    \UseInstance { wu / cover } { cover-i-en }
%  }
  
\NewDocumentCommand \makecoveri { }
  {
    \tl_if_eq:NnTF \g__wu_thesis_type_tl { proposal }
      {
        % --- Proposal 类型逻辑 ---
        \thispagestyle { empty }
        \UseInstance { wu / cover } { cover-proposal-default }
        \clearpage
        \__wu_cover_proposal_sign:
      }
      {
        % --- 原有逻辑 (bachelor/master/doctor) ---
        % 1. 生成中文封面
        \thispagestyle { empty }
        \tl_set:Nn \thepage { A }
        \UseInstance { wu / cover } { cover-i-default }
        % 2. 换页并生成英文封面
        \newpage 
        \thispagestyle { empty }
        \UseInstance { wu / cover } { cover-i-en }
      }
  }
  
\NewDocumentCommand \makecoverii { }
  {
    \thispagestyle { empty }
    \tl_set:Nn \thepage { B }
    \clist_if_empty:NTF \l__wu_info_instructors_clist
      { \hbox:n { } }
      { \UseInstance { wu / cover } { cover-ii-default } }
  }
\NewDocumentCommand \makecoveriii { }
  {
    \cleardoublepage
    \thispagestyle { empty }
    \tl_set:Nn \thepage { C }
    \tl_if_empty:NTF \l__wu_declaration_page_tl
      { \UseInstance { wu / cover } { cover-iii-default } }
      { \includepdf { \l__wu_declaration_page_tl } }
  }
\DeclareCoverTemplate { cover-i   }
  { id, logo, type, degree, title, title-en, info, date }

%增加proposal cover
\DeclareCoverTemplate { cover-proposal }
  { id, logo, type, title, info, signature, footer }
  
\DeclareCoverTemplate { cover-ii  } { title, name-list }
\DeclareCoverTemplate { cover-iii }
  {
    originality-decl-name,
    originality-decl-text,
    originality-decl-sig,
    authorization-decl-name,
    authorization-decl-text,
    authorization-decl-sig
  }
\DeclareInstance { wu / cover } { cover-i-default } { cover-i }
  {
    bottom-skip            = 0 pt plus 1.5 fill,
    id       / content     = \__wu_cover_id:,
    logo     / content     = \__wu_cover_logo:,
    type     / content     = \__wu_cover_type:,
    degree   / content     = \__wu_cover_degree:,
    title    / content     =
      \__wu_fixed_width_center_box:nn
        { 0.9 \textwidth } { \l__wu_info_title_tl },
%    title-en / content     =
%      \__wu_fixed_width_center_box:nn
%        { 0.9 \textwidth } { \l__wu_info_title_en_tl },
    info     / content     = \__wu_cover_info:,
    info    /format  =  \zihao{ 3 } \ttfamily,
    
     % --- 新增日期的配置 ---
    date     / content     = \l__wu_info_date_tl,  % 读取 info/date 中的内容
    date     / format      = \zihao{3}, % 设置字号为三号，字体为宋体(根据需要调整)
    date     / align       = center,               % 居中对齐
    date     / bottom-skip = 0 pt,                 % 日期下方不再需要大量空白
    % --------------------
    
    id       / format      = \zihao { -5 },
    type     / format      = \zihao {  2 },
    degree   / format      = \zihao {  4 },
    title    / format      = \zihao { 1 } \sffamily \linespread { 1.25 } \selectfont,
%    title-en / format      =
%      \__wu_line_spread:n { 1.2 } \zihao { 4 } \bfseries,
    id       / bottom-skip = 0 pt plus 1.6 fill,
    logo     / bottom-skip = 0 pt plus 0.3 fill,
    type     / bottom-skip = -18 pt,
    degree   / bottom-skip = 0 pt plus 0.8 fill,
%    title-en / bottom-skip = 0 pt plus 2.5 fill,
    
    info     / bottom-skip = 0 pt plus 2.0 fill,

    id       / align       = right,
    logo     / align       = center,
    type     / align       = center,
    degree   / align       = center,
    title    / align       = center,
    title-en / align       = center,
    info     / align       = center,
  }
% 添加英文封面
\DeclareInstance { wu / cover } { cover-i-en } { cover-i }
  {
    bottom-skip            = 0 pt plus 1.5 fill,
    id       / content     = \c_empty_tl,          % 英文封面通常不放学号代码块，如需要可改为 \__wu_cover_id:
    logo     / content     = \__wu_cover_logo:,
    type     / content     = \__wu_cover_type_en:, % 使用上面定义的英文类型
    degree   / content     = \c_empty_tl,
    
    date   / content     = \c_empty_tl, %  不显示中文日期
    
    % 将主标题设置为英文标题变量
    title    / content     =
      \__wu_fixed_width_center_box:nn
        { 0.9 \textwidth } { \l__wu_info_title_en_tl },
        
    % 清空副标题（原位置通常放英文标题，现在主标题已经是英文了）
    title-en / content     = \c_empty_tl,
    
    % 使用上面定义的英文信息表
    info     / content     = \__wu_cover_info_en:,
    info    / format  =  \zihao { 3 },
    % 格式设置 (沿用中文封面的字号设置，可根据需要调整)
    type     / format      = \zihao { -2 } ,
    title    / format      = \zihao { 1 } \bfseries, 
    
    % 间距与对齐 (沿用默认)
    id       / bottom-skip = 0 pt plus 1.6 fill,
    logo     / bottom-skip = 0 pt plus 0.3 fill,
    type     / bottom-skip = 0 pt plus 0.8 fill, % 调整间距
    degree   / bottom-skip = 0 pt,
    title    / bottom-skip = 0 pt plus 2.5 fill,
    title-en / bottom-skip = 0 pt,
    
    id       / align       = right,
    logo     / align       = center,
    type     / align       = center,
    degree   / align       = center,
    title    / align       = center,
    title-en / align       = center,
    info     / align       = center,
  }
% -------------------------------------------------------------

\DeclareInstance { wu / cover } { cover-proposal-default } { cover-proposal }
  {
    % --- 新增：学号与学校代码 (右上角) ---
    id       / content     = \__wu_cover_id:,
    id       / format      = \zihao { -5 },
    id       / align       = right,
    % 这里的 skip 设置为 fill，会将下方的内容(logo)推向页面垂直居中的位置，类似于 cover-i
    id       / bottom-skip = 0 pt plus 1.6 fill, 
    % ----------------------------------

    logo     / content     = \__wu_cover_logo:,
    logo     / align       = center,
    logo     / bottom-skip = 0 pt plus 0.5 fill,

    % --- 修改：论文类型 (包含您指定的格式命令) ---
    type     / content     = {\zihao{2} 本科生毕业论文（设计）\\ 文献综述和开题报告 },
    % 因为 content 里已经有了字号和字体，这里只需要设置行距
    type     / format      = \linespread{1.5}\selectfont, 
    type     / align       = center,
    type     / bottom-skip = 0 pt plus 1.5 fill,
    % ----------------------------------------

    title    / content     =
      \__wu_fixed_width_center_box:nn
        { 0.9 \textwidth } { \l__wu_info_title_tl },
    title    / format      = \zihao { 1 } \sffamily,
    title    / align       = center,
    title    / bottom-skip = 0 pt plus 2 fill,

    info     / content     = \__wu_cover_info_proposal:,
    info     / format      = \zihao{ 3 } \ttfamily,
    info     / align       = center,
    info     / bottom-skip = 0 pt plus 2 fill,
    
    % 添加 footer 的内容和格式
    footer / content = { 西湖大学教学事务部制 },
    footer / format  = \zihao{3}  \ttfamily,
    footer / align   = center,
    footer / bottom-skip = 1cm, 
  }
  
\DeclareInstance { wu / cover } { cover-ii-default } { cover-ii }
  {
    title     / content =
      \__wu_spread_box:no { 7 em } { \c__wu_name_instructors_tl },
    name-list / content =
      \clist_use:Nn \l__wu_info_instructors_clist { \par },
    title     / format  = \zihao { 2 } \sffamily,
    name-list / format  = \large,
    title     / align   = center,
    name-list / align   = center,
  }
\DeclareInstance { wu / cover } { cover-iii-default } { cover-iii }
  {
    format                                =
      \__wu_line_spread:n { 1.8 },
    top-skip                              = 0 pt plus 0.2 fill,
    bottom-skip                           = 0 pt plus 2.5 fill,
    originality-decl-name   / content     = \c__wu_name_orig_decl_tl,
    originality-decl-text   / content     = \c__wu_orig_decl_text_tl,
    originality-decl-sig    / content     =
      \__wu_cover_signature:N \c__wu_orig_decl_sign_clist,
    authorization-decl-name / content     = \c__wu_name_auth_decl_tl,
    authorization-decl-text / content     = \c__wu_auth_decl_text_tl,
    authorization-decl-sig  / content     =
      \__wu_cover_signature:N \c__wu_auth_decl_sign_clist,
    originality-decl-name   / format      =
      \__wu_line_spread:n { 1.2 } \zihao { -2 } \bfseries,
    authorization-decl-name / format      =
      \__wu_line_spread:n { 1.2 } \zihao { -2 } \bfseries,
      
    %originality-decl-text   / format =  \ttfamily,
    %authorization-decl-text / format =  \ttfamily,
     
    originality-decl-name   / bottom-skip = 0.4 cm,
    originality-decl-text   / bottom-skip = 0.4 cm,
    originality-decl-sig    / bottom-skip = 0 pt plus 2.5 fill,
    authorization-decl-name / bottom-skip = 0.4 cm,
    authorization-decl-text / bottom-skip = 0.4 cm,
    originality-decl-name   / align       = center,
    originality-decl-sig    / align       = right,
    authorization-decl-name / align       = center,
    authorization-decl-sig  / align       = right,
  }
\bool_new:N \l__wu_auto_make_cover_bool
\tl_new:N   \l__wu_declaration_page_tl
\keys_define:nn { wu / style }
  {
    auto-make-cover  .bool_set:N = \l__wu_auto_make_cover_bool,
    auto-make-cover  .default:n  = true,
    declaration-page .code:n     =
      {
        \tl_set_eq:NN \l__wu_declaration_page_tl \l_keys_value_tl
        \RequirePackage { pdfpages }
      },
  }
\ctex_after_end_preamble:n
  {
    \bool_if:NT \l__wu_auto_make_cover_bool
      {
         \begin{titlepage}
          % 步骤1：始终生成主封面
          \makecoveri 
          
          % 步骤2：生成指导小组名单 (Cover II)
          % 只要“指导小组(instructors)”列表不为空，任何类型的论文都生成这一页。
          \clist_if_empty:NF \l__wu_info_instructors_clist
            {
              \newpage 
              \makecoverii 
            }
        \end{titlepage}
      }
  }

\__wu_gadd_ltxhook:nn { enddocument }
  {
    \bool_if:NT \l__wu_auto_make_cover_bool
      {
        \tl_if_eq:NnF \g__wu_thesis_type_tl { proposal }
          {
            \makecoveriii   % 输出独创性声明
          }
      }
  }
    
%\__wu_gadd_ltxhook:nn { enddocument }
%  { \bool_if:NT \l__wu_auto_make_cover_bool { \makecoveriii } }
\keys_set:nn { ctex }
  {
    contentsname   = \c__wu_name_toc_tl,
    listfigurename = \c__wu_name_lof_tl,
    listtablename  = \c__wu_name_lot_tl,
    chapter / tocline =
      {
        \normalfont \sffamily
        \CTEXnumberline {#1} #2
      },
    section / tocline =
      {
        \CTEXnumberline {#1} #2
      },
    subsection / tocline =
      {
        \wu@kai
        \CTEXnumberline {#1} #2
      }
  }
\__wu_patch_cmd:Nnn \tableofcontents
  {
    \chapter*{\contentsname
      \@mkboth{\MakeUppercase\contentsname}
              {\MakeUppercase\contentsname}}
  }
  { \__wu_chapter_no_toc:V \contentsname }
\__wu_patch_cmd:Nnn \listoffigures
  {
    \chapter*{\listfigurename}
    \@mkboth{\MakeUppercase\listfigurename}
            {\MakeUppercase\listfigurename}
  }
  { \__wu_chapter:V \listfigurename }
\__wu_patch_cmd:Nnn \listoftables
  {
    \chapter*{\listtablename}
    \@mkboth{\MakeUppercase\listtablename}
            {\MakeUppercase\listtablename}
  }
  { \__wu_chapter:V \listtablename }
\NewDocumentEnvironment { abstract  } { }
  { \__wu_abstract_begin:    } { \__wu_abstract_end:      }
\NewDocumentEnvironment { abstract* } { }
  { \__wu_abstract_en_begin: } { \__wu_abstract_en_end:   }
\cs_new_protected:Npn \__wu_abstract_begin:
  {
    \group_begin:
      \cs_set_protected:Npn \chaptermark ##1
        { \markboth {##1} {##1} }
      \__wu_chapter:V \c__wu_name_abstract_tl
    \group_end:
    \thispagestyle { fancy }
  }

\cs_new_protected:Npn \__wu_abstract_en_begin:
  {
    \group_begin:
      \cs_set_protected:Npn \chaptermark ##1
        { \markboth {##1} {##1} }
      \__wu_chapter:V \c__wu_name_abstract_en_tl
    \group_end:
    \thispagestyle { fancy }
  }
\cs_new_protected:Npn \__wu_abstract_end:
  {
    \__wu_keywords:nNn
      { \sffamily \c__wu_name_keywords_tl \c__wu_fwid_colon_tl }
      \l__wu_info_keywords_clist { \c__wu_fwid_semicolon_tl }
    \tl_if_empty:NF \l__wu_info_clc_tl
      {
        \__wu_clc_jel:nn
          { \sffamily \c__wu_name_clc_tl \c__wu_fwid_colon_tl }
          { \l__wu_info_clc_tl }
      }
  }
\cs_new_protected:Npn \__wu_abstract_en_end:
  {
    \__wu_keywords:nNn
      { \bfseries \c__wu_name_keywords_en_tl \__wu_quad: }
      \l__wu_info_keywords_en_clist { ; ~ }
    \tl_if_empty:NTF \l__wu_info_jel_tl
      {
        \tl_if_empty:NF \l__wu_info_clc_tl
          {
            \__wu_clc_jel:nn
              { \bfseries \c__wu_name_clc_en_tl \__wu_quad: }
              { \l__wu_info_clc_tl }
          }
      }
      {
        \__wu_clc_jel:nn
          { \bfseries \c__wu_name_jel_en_tl \__wu_quad: }
          { \l__wu_info_jel_tl }
      }
  }
\cs_new_protected:Npn \__wu_keywords:nNn #1#2#3
  {
    \par \mode_leave_vertical: \par \noindent
    \__wu_get_text_width:Nn \l__wu_tmpa_dim {#1}
    \group_begin: #1 \group_end:
    \parbox [t] { \dim_eval:n { \textwidth - \l__wu_tmpa_dim } }
      {
        \clist_use:Nn #2 {#3} \par
        \cs_gset:Npx \__wu_keywords_prevdepth:
          { \dim_use:N \tex_prevdepth:D }
      }
  }
\cs_new_protected:Npn \__wu_clc_jel:nn #1#2
  {
    \par \tex_prevdepth:D \__wu_keywords_prevdepth: \noindent
    \group_begin: #1 \group_end:
    #2
  }
\NewDocumentEnvironment { notation } { O { l p { 7.5 cm } } }
  {
    \__wu_notation_begin:
    \group_begin:
      \__wu_notation_long_table_setup:
      \longtable {#1}
  }
  {
      \endlongtable
    \group_end:
  }
\cs_new_protected:Npn \__wu_notation_begin:
  {
    \__wu_chapter:V \c__wu_name_notation_tl
  }
\cs_new_protected:Npn \__wu_notation_long_table_setup:
  {
    \dim_set_eq:NN \LTpre  \c_zero_dim
    \dim_set_eq:NN \LTpost \c_zero_dim
  }
\NewDocumentEnvironment { acknowledgements } { }
  { \__wu_acknowledgements_begin: } { }
\cs_new_protected:Npn \__wu_acknowledgements_begin:
  {
    \__wu_chapter:V \c__wu_name_acknowledgements_tl
  }
\tl_new:N \l__wu_bib_backend_tl
\tl_new:N \l__wu_bib_style_tl
\tl_new:N \l__wu_bib_gb_style_tl
\tl_new:N \l__wu_cite_style_tl
\clist_new:N \l__wu_bib_resource_clist
\keys_define:nn { wu / style }
  {
    bib-backend .choice:,
    bib-backend .value_required:n = true,
    bib-backend / bibtex   .code:n =
      { \tl_set:Nn \l__wu_bib_backend_tl { bibtex } },
    bib-backend / biblatex .code:n =
      {
        \tl_set:Nn \l__wu_bib_backend_tl { biblatex }
        \NewDocumentCommand \addbibresource { m }
          { \clist_gput_right:Nn \l__wu_bib_resource_clist {#1} }
      },
    bib-style .choice:,
    bib-style .value_required:n = true,
    bib-style / numerical    .code:n =
      {
        \tl_set:Nn  \l__wu_bib_gb_style_tl { numerical  }
        \tl_clear:N \l__wu_bib_style_tl
      },
    bib-style / author-year .code:n =
      {
        \tl_set:Nn  \l__wu_bib_gb_style_tl { author-year }
        \tl_clear:N \l__wu_bib_style_tl
      },
    bib-style / unknown     .code:n =
      {
        \tl_set_eq:NN \l__wu_bib_style_tl \l_keys_value_tl
        \tl_clear:N   \l__wu_bib_gb_style_tl
      },
    cite-style .tl_set:N = \l__wu_cite_style_tl,
    bib-resource .clist_set:N = \l__wu_bib_resource_clist
  }
\ctex_at_end_preamble:n
  {
    \tl_if_eq:NnT \l__wu_bib_backend_tl { bibtex }
      {
        \tl_if_empty:NTF \l__wu_bib_style_tl
          {
            \RequirePackage [ sort & compress ] { gbt7714 }
            \exp_args:No \bibliographystyle
              { gbt7714- \l__wu_bib_gb_style_tl }
          }
          {
            \RequirePackage [ sort & compress ] { natbib }
            \exp_args:No \bibliographystyle
              { \l__wu_bib_style_tl }
          }
        \__wu_bibtex_setup:
      }
  }
\__wu_gadd_ltxhook:nn { env/document/begin }
  {
    \tl_if_eq:NnT \l__wu_bib_backend_tl { biblatex }
      {
        \__wu_biblatex_pre_setup:
        \RequirePackage { biblatex }
        \__wu_biblatex_post_setup:
      }
  }
\cs_new_protected:Npn \__wu_bibtex_setup:
  {
    \tl_if_eq:VnTF \l__wu_bib_gb_style_tl { numerical }
      {
        \exp_args:NNx \DeclareRobustCommand \parencite
          { \exp_args:No \exp_not:o { \cs:w cite ~ \cs_end: } }
        \exp_args:Nc \ctex_patch_cmd:Nnn { parencite ~ }
          { \begingroup }
          { \begingroup \bibstyle@numbers }
      }
      { \cs_set_eq:NN \parencite \cite }
    \tl_if_empty:NF \l__wu_cite_style_tl
      { \exp_args:NV \citestyle \l__wu_cite_style_tl }
    \ctex_patch_cmd:Nnn \NAT@citexnum
      { - \NAT@penalty }
      { \textendash \NAT@penalty }
    \cs_set:Npn \bibsection { \__wu_chapter:V \bibname }
    \NewDocumentCommand \printbibliography { o }
      {
        \exp_args:NV \bibliography \l__wu_bib_resource_clist
        \IfValueT {##1}
          { \__wu_warning:nn { invalid-option-in-bibtex } {##1} }
      }
  }
\__wu_msg_new:nn { invalid-option-in-bibtex }
  { Option(s)~ "#1"~ are~ invalid~ in~ BibTeX. }
\cs_new_protected:Npn \__wu_biblatex_pre_setup:
  {
    \cs_undefine:N \addbibresource
    \clist_new:N \l__wu_biblatex_options_clist
    \clist_put_right:Nn \l__wu_biblatex_options_clist { hyperref = manual }
    \clist_put_right:Nx \l__wu_biblatex_options_clist
      {
        style =
        \tl_if_empty:NTF \l__wu_bib_style_tl
          {
            \str_if_eq:VnTF \l__wu_bib_gb_style_tl { numerical }
              { gb7714-2015 } { gb7714-2015ay }
          }
          { \l__wu_bib_style_tl }
      }
    \tl_if_empty:NF \l__wu_cite_style_tl
      {
        \clist_put_right:Nx \l__wu_biblatex_options_clist
          { citestyle = \l__wu_cite_style_tl }
      }
    \exp_args:NV \PassOptionsToPackage \l__wu_biblatex_options_clist
      { biblatex }
  }
\cs_new_protected:Npn \__wu_biblatex_post_setup:
  {
    \clist_map_function:NN \l__wu_bib_resource_clist \addbibresource
    \__wu_biblatex_allow_url_break:
    \__wu_biblatex_use_en_dash:
    \defbibheading { bibliography } [ \bibname ] { \__wu_chapter:n {##1} }
  }
\cs_new:Npn \__wu_biblatex_allow_url_break:
  {
    \int_set_eq:NN \c@biburlucpenalty  \c_one_int
    \int_set_eq:NN \c@biburlnumpenalty \c_one_int
    \int_set_eq:NN \c@biburllcpenalty  \c_one_int
  }
\cs_new:Npn \__wu_biblatex_use_en_dash:
  {
    \DefineBibliographyExtras { english }
      {
        \cs_set_nopar:Npn \bibrangedash
          { \textendash \penalty \hyphenpenalty }
      }
    \DefineBibliographyExtras { russian }
      {
        \cs_set_nopar:Npn \bibrangedash
          { \textendash \penalty \hyphenpenalty }
      }
  }
\DeclareDocumentCommand \hypersetup { m }
  { \wu_hyperref_setup:n {#1} }
\cs_new_protected:Npn \wu_hyperref_setup:n #1
  { \clist_gput_right:Nn \g__wu_to_hyperref_clist {#1} }
\cs_new:Npn \__wu_set_hyperlink_color_key:n #1
  {
    hyperlink-color / \clist_item:nn {#1} {1} .code:n =
      {
        \__wu_define_hyperlink_color:nnn
          { \clist_item:nn {#1} {2} }
          { \clist_item:nn {#1} {3} }
          { \clist_item:nn {#1} {4} }
        \wu_hyperref_setup:n
          {
            linkcolor = wu@link, linkbordercolor = wu@link,
            urlcolor  = wu@url,  urlbordercolor  = wu@url,
            citecolor = wu@cite, citebordercolor = wu@cite
          }
      },
  }
\cs_new_protected:Npn \__wu_define_hyperlink_color:nnn #1#2#3
  {
    \definecolorset { HTML } { wu@ } { }
      { link, #1; url, #2; cite, #3 }
  }
\keys_define:nx { wu / style }
  {
    hyperlink .choice:,
    hyperlink .value_required:n = true,
    hyperlink / border .code:n =
      { \wu_hyperref_setup:n { colorlinks = false } },
    hyperlink / color  .code:n =
      { \wu_hyperref_setup:n { colorlinks = true  } },
    hyperlink / none   .code:n =
      { \wu_hyperref_setup:n { hidelinks } },
    hyperlink-color .choice:,
    hyperlink-color .value_required:n = true,
    \clist_map_function:nN
      {
        { classic,   FF0000, 0000FF, 00FF00 },
        { default,   990000, 0000B2, 007F00 },
        { material,  E91E63, 009688, 4CAF50 },
        { graylevel, 616161, 616161, 616161 },
        { prl,       2D3092, 2D3092, 2D3092 }
      }
      \__wu_set_hyperlink_color_key:n
  }
\cs_new:Npn \wu_allow_url_break:
  {
    \cs_new:Npn \__wu_add_url_break_points:
      { \tl_map_function:NN \c__wu_url_break_points_tl \do }
    \__wu_appto_cmd:Nn \UrlBreaks
      { \UrlOrds \__wu_add_url_break_points: }
  }
\tl_const:Nn \c__wu_url_break_points_tl
  {
    abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    0123456789
  }
\ctex_at_end_preamble:n
  {
    \RequirePackage { hyperref }
    \hypersetup
      {
        bookmarksnumbered = true,
        psdextra          = true,
        unicode           = true,
        pdftitle    = \l__wu_info_title_sanitized_tl,
        pdfauthor   = \l__wu_info_author_tl,
        pdfkeywords = \l__wu_info_keywords_clist,
        pdfcreator  = \c__wu_name_pdf_creator_tl
      }
    \exp_args:NV \hypersetup \g__wu_to_hyperref_clist
    \wu_allow_url_break:
    \tl_if_eq:NnT \l__wu_bib_backend_tl { biblatex }
      { \BiblatexManualHyperrefOn }
  }
\ctex_at_end_package:nn { hyperref }
  {
    \pdfstringdefDisableCommands
      {
        \cs_set_eq:NN \wu@kai \prg_do_nothing:
        \cs_set_eq:NN \quad    \c_space_tl
        \cs_set_eq:NN \qquad   \c_space_tl
      }
  }
\keys_define:nn { wu }
  {
    info  .meta:nn = { wu / info  } {#1},
    style .meta:nn = { wu / style } {#1}
  }
\keys_set:nn { wu }
  {
    style   / font            = times,
    style   / cjk-font        = fandol,
    style   / font-size       = -4,
    style   / fullwidth-stop  = false,
    style   / auto-make-cover = true,
    style   / logo            = { westlake-logo.pdf },
    style   / logo-size       = { 0.5 \textwidth },
    style   / hyperlink       = color,
    style   / hyperlink-color = default,
    style   / bib-style       = numerical,
    info    / degree          = academic,
    info    / secret-level    = none,
    info    / school-id       = { 14626 },
    info    / date            = { \zhtoday },
    theorem / header-font     = { \sffamily },
    theorem / body-font       = { \wu@kai },
    theorem / counter         = { chapter }
  }
\NewDocumentCommand \wusetup { m }
  { \keys_set:nn { wu } {#1} }
\newtheorem* { proof       } { \c__wu_name_proof_tl      }
\newtheorem  { axiom       } { \c__wu_name_axiom_tl      }
\newtheorem  { corollary   } { \c__wu_name_corollary_tl  }
\newtheorem  { definition  } { \c__wu_name_definition_tl }
\newtheorem  { example     } { \c__wu_name_example_tl    }
\newtheorem  { lemma       } { \c__wu_name_lemma_tl      }
\newtheorem  { theorem     } { \c__wu_name_theorem_tl    }
\endinput
%%
%% End of file `wuthesis.cls'.

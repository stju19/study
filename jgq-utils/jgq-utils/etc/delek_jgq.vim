" Vim color file - delek_modified
" Generated by http://bytefluent.com/vivify 2015-08-17
set background=dark
if version > 580
	hi clear
	if exists("syntax_on")
		syntax reset
	endif
endif

set t_Co=256
let g:colors_name = "delek_modified"

"hi IncSearch -- no settings --
"hi SignColumn -- no settings --
"hi TabLineSel -- no settings --
"hi CTagsMember -- no settings --
"hi CTagsGlobalConstant -- no settings --
"hi Ignore -- no settings --
"hi PMenuSbar -- no settings --
"hi Todo -- no settings --
hi Normal guifg=#000000 guibg=#ffffff guisp=#ffffff gui=NONE ctermfg=NONE ctermbg=15 cterm=NONE
"hi CTagsImport -- no settings --
"hi Search -- no settings --
"hi CTagsGlobalVariable -- no settings --
"hi SpellRare -- no settings --
"hi EnumerationValue -- no settings --
"hi Float -- no settings --
"hi CursorLine -- no settings --
"hi Union -- no settings --
"hi TabLineFill -- no settings --
"hi CursorColumn -- no settings --
"hi EnumerationName -- no settings --
"hi SpellCap -- no settings --
"hi VertSplit -- no settings --
"hi DiffChange -- no settings --
"hi Cursor -- no settings --
"hi SpellLocal -- no settings --
"hi Error -- no settings --
"hi DefinedName -- no settings --
"hi PMenuThumb -- no settings --
"hi MatchParen -- no settings --
"hi LocalVariable -- no settings --
"hi SpellBad -- no settings --
"hi CTagsClass -- no settings --
"hi Underlined -- no settings --
"hi DiffAdd -- no settings --
"hi TabLine -- no settings --
"hi clear -- no settings --
hi WildMenu guifg=#000000 guibg=NONE guisp=NONE gui=NONE ctermfg=NONE ctermbg=NONE cterm=NONE
hi SpecialComment guifg=#ff1493 guibg=NONE guisp=NONE gui=NONE ctermfg=198 ctermbg=NONE cterm=NONE
hi Typedef guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi Title guifg=#ff00ff guibg=NONE guisp=NONE gui=bold ctermfg=201 ctermbg=NONE cterm=bold
hi Folded guifg=#00008b guibg=NONE guisp=NONE gui=NONE ctermfg=18 ctermbg=NONE cterm=NONE
hi PreCondit guifg=#cd00cd guibg=NONE guisp=NONE gui=NONE ctermfg=164 ctermbg=NONE cterm=NONE
hi Include guifg=#cd00cd guibg=NONE guisp=NONE gui=NONE ctermfg=164 ctermbg=NONE cterm=NONE
hi StatusLineNC guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi NonText guifg=#bebebe guibg=NONE guisp=NONE gui=bold ctermfg=7 ctermbg=NONE cterm=bold
hi DiffText guifg=NONE guibg=NONE guisp=NONE gui=bold ctermfg=NONE ctermbg=NONE cterm=bold
hi ErrorMsg guifg=#ffffff guibg=NONE guisp=NONE gui=NONE ctermfg=15 ctermbg=NONE cterm=NONE
hi Debug guifg=#ff1493 guibg=NONE guisp=NONE gui=NONE ctermfg=198 ctermbg=NONE cterm=NONE
hi Identifier guifg=#008b8b guibg=NONE guisp=NONE gui=NONE ctermfg=30 ctermbg=NONE cterm=NONE
hi SpecialChar guifg=#ff1493 guibg=NONE guisp=NONE gui=NONE ctermfg=198 ctermbg=NONE cterm=NONE
hi Conditional guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi StorageClass guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi Special guifg=#ff1493 guibg=NONE guisp=NONE gui=NONE ctermfg=198 ctermbg=NONE cterm=NONE
hi LineNr guifg=#a52a2a guibg=NONE guisp=NONE gui=NONE ctermfg=124 ctermbg=NONE cterm=NONE
hi StatusLine guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi Label guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi PMenuSel guifg=#0000ff guibg=NONE guisp=NONE gui=NONE ctermfg=21 ctermbg=NONE cterm=NONE
hi Delimiter guifg=#ff1493 guibg=NONE guisp=NONE gui=NONE ctermfg=198 ctermbg=NONE cterm=NONE
hi Statement guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi Comment guifg=#ee0000 guibg=NONE guisp=NONE gui=NONE ctermfg=196 ctermbg=NONE cterm=NONE
hi Character guifg=#00cd00 guibg=NONE guisp=NONE gui=NONE ctermfg=40 ctermbg=NONE cterm=NONE
hi Number guifg=#00cd00 guibg=NONE guisp=NONE gui=NONE ctermfg=40 ctermbg=NONE cterm=NONE
hi Boolean guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi Operator guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi Question guifg=#2e8b57 guibg=NONE guisp=NONE gui=bold ctermfg=29 ctermbg=NONE cterm=bold
hi WarningMsg guifg=#ff0000 guibg=NONE guisp=NONE gui=NONE ctermfg=196 ctermbg=NONE cterm=NONE
hi VisualNOS guifg=NONE guibg=NONE guisp=NONE gui=bold,underline ctermfg=NONE ctermbg=NONE cterm=bold,underline
hi DiffDelete guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi ModeMsg guifg=NONE guibg=NONE guisp=NONE gui=bold ctermfg=NONE ctermbg=NONE cterm=bold
hi Define guifg=#cd00cd guibg=NONE guisp=NONE gui=NONE ctermfg=164 ctermbg=NONE cterm=NONE
hi Function guifg=#008b8b guibg=NONE guisp=NONE gui=NONE ctermfg=30 ctermbg=NONE cterm=NONE
hi FoldColumn guifg=#00008b guibg=NONE guisp=NONE gui=NONE ctermfg=18 ctermbg=NONE cterm=NONE
hi PreProc guifg=#cd00cd guibg=NONE guisp=NONE gui=NONE ctermfg=164 ctermbg=NONE cterm=NONE
hi Visual guifg=#bebebe guibg=#000000 guisp=#000000 gui=NONE ctermfg=7 ctermbg=NONE cterm=NONE
hi MoreMsg guifg=#2e8b57 guibg=NONE guisp=NONE gui=bold ctermfg=29 ctermbg=NONE cterm=bold
hi Exception guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi Keyword guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi Type guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi PMenu guifg=#0000ff guibg=NONE guisp=NONE gui=NONE ctermfg=21 ctermbg=NONE cterm=NONE
hi SpecialKey guifg=#0000ff guibg=NONE guisp=NONE gui=NONE ctermfg=21 ctermbg=NONE cterm=NONE
hi Constant guifg=#00cd00 guibg=NONE guisp=NONE gui=NONE ctermfg=40 ctermbg=NONE cterm=NONE
hi Tag guifg=#ff1493 guibg=NONE guisp=NONE gui=NONE ctermfg=198 ctermbg=NONE cterm=NONE
hi String guifg=#00cd00 guibg=NONE guisp=NONE gui=NONE ctermfg=40 ctermbg=NONE cterm=NONE
hi Repeat guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi Directory guifg=#0000ff guibg=NONE guisp=NONE gui=NONE ctermfg=21 ctermbg=NONE cterm=NONE
hi Structure guifg=#0000ff guibg=NONE guisp=NONE gui=bold ctermfg=21 ctermbg=NONE cterm=bold
hi Macro guifg=#cd00cd guibg=NONE guisp=NONE gui=NONE ctermfg=164 ctermbg=NONE cterm=NONE
hi cursorim guifg=#000000 guibg=#a0a0c0 guisp=#a0a0c0 gui=NONE ctermfg=NONE ctermbg=103 cterm=NONE
hi lcursor guifg=NONE guibg=#00ffff guisp=#00ffff gui=NONE ctermfg=NONE ctermbg=14 cterm=NONE
hi method guifg=#0000ff guibg=NONE guisp=NONE gui=NONE ctermfg=21 ctermbg=NONE cterm=NONE
hi user1 guifg=#00ff8b guibg=#3e3e5e guisp=#3e3e5e gui=NONE ctermfg=48 ctermbg=60 cterm=NONE
hi mbenormal guifg=#cfbfad guibg=#2e2e3f guisp=#2e2e3f gui=NONE ctermfg=187 ctermbg=237 cterm=NONE
hi perlspecialstring guifg=#c080d0 guibg=#404040 guisp=#404040 gui=NONE ctermfg=176 ctermbg=238 cterm=NONE
hi doxygenspecial guifg=#fdd090 guibg=NONE guisp=NONE gui=NONE ctermfg=222 ctermbg=NONE cterm=NONE
hi mbechanged guifg=#eeeeee guibg=#2e2e3f guisp=#2e2e3f gui=NONE ctermfg=255 ctermbg=237 cterm=NONE
hi mbevisiblechanged guifg=#eeeeee guibg=#4e4e8f guisp=#4e4e8f gui=NONE ctermfg=255 ctermbg=60 cterm=NONE
hi doxygenparam guifg=#fdd090 guibg=NONE guisp=NONE gui=NONE ctermfg=222 ctermbg=NONE cterm=NONE
hi doxygensmallspecial guifg=#fdd090 guibg=NONE guisp=NONE gui=NONE ctermfg=222 ctermbg=NONE cterm=NONE
hi doxygenprev guifg=#fdd090 guibg=NONE guisp=NONE gui=NONE ctermfg=222 ctermbg=NONE cterm=NONE
hi perlspecialmatch guifg=#c080d0 guibg=#404040 guisp=#404040 gui=NONE ctermfg=176 ctermbg=238 cterm=NONE
hi cformat guifg=#c080d0 guibg=#404040 guisp=#404040 gui=NONE ctermfg=176 ctermbg=238 cterm=NONE
hi doxygenspecialmultilinedesc guifg=#ad600b guibg=NONE guisp=NONE gui=NONE ctermfg=130 ctermbg=NONE cterm=NONE
hi taglisttagname guifg=#808bed guibg=NONE guisp=NONE gui=NONE ctermfg=105 ctermbg=NONE cterm=NONE
hi doxygenbrief guifg=#fdab60 guibg=NONE guisp=NONE gui=NONE ctermfg=215 ctermbg=NONE cterm=NONE
hi mbevisiblenormal guifg=#cfcfcd guibg=#4e4e8f guisp=#4e4e8f gui=NONE ctermfg=252 ctermbg=60 cterm=NONE
hi user2 guifg=#7070a0 guibg=#3e3e5e guisp=#3e3e5e gui=NONE ctermfg=103 ctermbg=60 cterm=NONE
hi doxygenspecialonelinedesc guifg=#ad600b guibg=NONE guisp=NONE gui=NONE ctermfg=130 ctermbg=NONE cterm=NONE
hi doxygencomment guifg=#ad7b20 guibg=NONE guisp=NONE gui=NONE ctermfg=130 ctermbg=NONE cterm=NONE
hi cspecialcharacter guifg=#c080d0 guibg=#404040 guisp=#404040 gui=NONE ctermfg=176 ctermbg=238 cterm=NONE
hi tagname guifg=#a7a7a7 guibg=#660000 guisp=#660000 gui=NONE ctermfg=248 ctermbg=52 cterm=NONE
hi titled guifg=#000000 guibg=#fffdfa guisp=#fffdfa gui=NONE ctermfg=NONE ctermbg=230 cterm=NONE
hi char guifg=#d0e080 guibg=#000000 guisp=#000000 gui=NONE ctermfg=186 ctermbg=NONE cterm=NONE
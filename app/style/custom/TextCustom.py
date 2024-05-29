from app import (
    ft
)

from app.style import *

from typing import List, Dict, Any, Tuple

from flet import TextSpan, TextOverflow



class TextCustom(ft.Text):
    def __init__(self, value: str | None = None, spans: List[TextSpan] | None = None, text_align: ft.TextAlign | None = None, font_family: str | None = None, size: None | int | float = None, weight: ft.FontWeight | None = None, italic: bool | None = None, style: ft.TextThemeStyle | ft.TextStyle | None = None, theme_style: ft.TextThemeStyle | None = None, max_lines: int | None = None, overflow: ft.TextOverflow = TextOverflow.NONE, selectable: bool | None = None, no_wrap: bool | None = None, color: str | None = None, bgcolor: str | None = None, semantics_label: str | None = None, ref: ft.Ref | None = None, key: str | None = None, width: None | int | float = None, height: None | int | float = None, left: None | int | float = None, top: None | int | float = None, right: None | int | float = None, bottom: None | int | float = None, expand: None | bool | int = None, expand_loose: bool | None = None, col: Dict[str, int | float] | int | float | None = None, opacity: None | int | float = None, rotate: None | int | float | ft.Rotate = None, scale: None | int | float | ft.Scale = None, offset: None | ft.Offset | Tuple[float | int, float | int] = None, aspect_ratio: None | int | float = None, animate_opacity: None | bool | int | ft.Animation = None, animate_size: None | bool | int | ft.Animation = None, animate_position: None | bool | int | ft.Animation = None, animate_rotation: None | bool | int | ft.Animation = None, animate_scale: None | bool | int | ft.Animation = None, animate_offset: None | bool | int | ft.Animation = None, on_animation_end=None, tooltip: str | None = None, visible: bool | None = None, disabled: bool | None = None, data: Any = None, rtl: bool | None = None):
        super().__init__(value, spans, text_align, font_family, size, weight, italic, style, theme_style, max_lines, overflow, selectable, no_wrap, PRIORITY, bgcolor, semantics_label, ref, key, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, visible, disabled, data, rtl)
        
        
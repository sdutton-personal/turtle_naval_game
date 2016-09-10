#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python $DIR"/interface_control_test.py"
python $DIR"/graphic_point_test.py"
python $DIR"/graphic_line_test.py"
python $DIR"/graphic_shape_test.py"

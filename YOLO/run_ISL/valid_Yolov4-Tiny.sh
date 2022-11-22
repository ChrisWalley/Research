if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ISL_data/obj.data cfg/yolov4-tiny-isl.cfg backup/yolov4-tiny-isl.backup < ISL_data/valid.txt > results/Yolov4-Tiny-isl_valid_cpu_results.txt
else
    ./darknet detector test ISL_data/obj.data cfg/yolov4-tiny-isl.cfg backup/yolov4-tiny-isl.backup < ISL_data/valid.txt > results/Yolov4-Tiny-isl_valid_results.txt
fi

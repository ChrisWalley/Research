if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ASL_data/obj.data cfg/yolov4-tiny.cfg backup/yolov4-tiny.backup < ASL_data/valid.txt > results/Yolov4-Tiny_valid_cpu_results.txt
else
    ./darknet detector test ASL_data/obj.data cfg/yolov4-tiny.cfg backup/yolov4-tiny.backup < ASL_data/valid.txt > results/Yolov4-Tiny_valid_results.txt
fi

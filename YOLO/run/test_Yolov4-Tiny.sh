if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ASL_data/obj.data cfg/yolov4-tiny.cfg backup/yolov4-tiny.backup < ASL_data/test.txt > results/Yolov4-Tiny_test_cpu_results.txt
else
    ./darknet detector test ASL_data/obj.data cfg/yolov4-tiny.cfg backup/yolov4-tiny.backup < ASL_data/test.txt > results/Yolov4-Tiny_test_results.txt
fi

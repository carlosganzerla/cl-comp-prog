;; Get the array, split in two, find the first item which is not supposed to be
;; in the half and calculate distance to middle. Increase middle by 1 and add
;; dist to 

(defun get-ans (arr n)
  (let ((sum 0)
        (out-of-place 0))
    (do ((i (1- n) (1- i))
         (swaps 0))
        ((< i 0) sum)
        (if (> (aref arr i) n)
            (progn
              (incf sum swaps)
              (incf out-of-place))
            (incf swaps)))
    (do ((i n (1+ i))
         (swaps 0))
        ((>= i (* 2 n)) (+ sum (* out-of-place out-of-place)))
        (if (<= (aref arr i) n)
            (incf sum swaps)
            (incf swaps)))))

(defun main ()
  (dotimes (_ (read))
    (let* ((n (read))
           (arr (make-array (* 2 n) :element-type 'fixnum)))
      (dotimes (i (length arr))
        (setf (aref arr i) (read)))
      (write (get-ans arr n))
      (terpri))))


(main)

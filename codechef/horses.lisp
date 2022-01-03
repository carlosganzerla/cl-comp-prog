(declaim (optimize (speed 3) (safety 0) (debug 0)))

(defun min-diff (s)
  (declare ((array fixnum) s))
  (let ((s (sort s #'>)))
    (do ((i 0 (1+ i))
         (min-diff 1000000000))
        ((>= i (1- (length s))) min-diff)
        (declare (fixnum i min-diff))
        (let ((diff (- (aref s i) (aref s (1+ i)))))
          (declare (fixnum diff))
          (when (< diff min-diff)
            (setf min-diff diff))))))

(declaim (inline min-diff))

(defun run ()
  (let ((s (make-array (read) :element-type 'fixnum)))
    (dotimes (i (length s) (format t "~A~%" (min-diff s)))
      (setf (aref s i) (read)))))

(dotimes (_ (read))
  (run))

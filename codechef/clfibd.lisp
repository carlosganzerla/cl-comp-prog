(declaim (optimize (speed 3) (safety 0) (debug 0)))

(defconstant +dynamic+ "Dynamic")
(defconstant +not+ "Not")

(defun check-dynamic (p)
  (print p)
  (when (< (length p) 3)
    (return-from check-dynamic +dynamic+))
  (dotimes (i (length p))
    (dotimes (j (length p))
      (dotimes (k (length p))
        (when (and (> k j i) (= (aref p k) (+ (aref p j) (aref p i))))
          (return-from check-dynamic +dynamic+)))))
  +not+)

(defun get-answer (str)
  (let ((table (make-array 26 :element-type 'fixnum)))
    (dotimes (i (length str) 
                (check-dynamic (remove-if #'zerop (sort table #'<))))
      (incf (aref table (- (char-code (aref str i)) 97))))))


(declaim (inline get-answer check-dynamic))

(defun main ()
  (dotimes (x (read))
    (format t "~A~%" (get-answer (read-line)))))

(main)

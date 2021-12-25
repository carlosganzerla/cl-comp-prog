(declaim (optimize (safety 0) (debug 0) (speed 3)))

(defvar *buffer* (make-array 1000000 :element-type 'fixnum))

(defun n-inc (n)
  (do ((carry 0)
       (i (1- (length n)) (1- i)))
      ((< i 0) (concatenate 'vector #(1) n))
      (let ((r (+ 1 (aref n i))))
        (setf (aref n i) (mod r 10))
        (if (> r 9)
            (setf carry 1)
            (return n)))))

(defun n> (n1 n2)
  (assert (= (length n1) (length n2)))
  (dotimes (i (length n1) nil)
    (cond ((> (aref n1 (- (length n1) 1 i)) (aref n2 i)) (return t))
          ((< (aref n1 (- (length n1) 1 i)) (aref n2 i)) (return nil)))))

(defun print-vec (n &optional (rev))
  (if rev
      (dotimes (i (length n)) (write (aref n (- (length n) 1 i))))
      (dotimes (i (length n)) (write (aref n i)))))


(defun get-ans (n)
  (let* ((lidx (floor (length n) 2))
         (ridx (ceiling (length n) 2))
         (l (subseq n 0 lidx))
         (r (subseq n ridx))
         (m (subseq n lidx ridx)))
    (if (or (<= (length n) 1) (n> l r))
        (progn (print-vec l) (print-vec m) (print-vec l t))
        (let ((inc (n-inc (concatenate 'vector l m))))
          (print-vec inc)
          (print-vec (subseq inc 0 (length l)) t))))
  (terpri))

(defun read-chars ()
  (do ((i 0 (1+ i))
       (c (- (char-code (read-char)) 48) (- (char-code (read-char)) 48)))
      ((or (< c 0) (> c 9)) (get-ans (subseq *buffer* 0 i)))
      (setf (aref *buffer* i) c)))

(defun main ()
  (dotimes (_ (read))
    (read-chars)))

(main)
